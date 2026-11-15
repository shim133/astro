import json, html, re, os, datetime, base64, sys, argparse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HOME_DIR = os.path.expanduser('~')

# Support both Antigravity Hub (~/.gemini/antigravity) and Antigravity IDE (~/.gemini/antigravity-ide)
BRAIN_DIRS = {
    'ag_hub': os.path.join(HOME_DIR, '.gemini', 'antigravity', 'brain'),
    'ag_ide': os.path.join(HOME_DIR, '.gemini', 'antigravity-ide', 'brain'),
}

# Current conversation ID for astroDating Expert Astrologist v2.5.0
DEFAULT_CONV_ID = '6ca4c9ae-3b8c-4305-90d1-698625680a3e'

SESSION_METADATA = {
    '6ca4c9ae': {
        'filename': 'chat_astromatch_v251_expert_astrologist_6ca4c9ae.html',
        'title': 'AstroMatch Pro v2.5.1: Single & Transit Mode, Balanced Synastry, Help Guide & Snapshot DB',
    },
    '6b1072ff': {
        'filename': 'chat_astromatch_v220_v241_foundation_6b1072ff.html',
        'title': 'AstroMatch Pro v2.2.0 - v2.4.1: Foundation, Bilingual UI, Porphyry Houses & Tropical/J2000 System',
    },
}


def resolve_conversation_paths(conv_or_path=None, prefer_env=None):
    """
    Resolves (transcript_path, user_upload_dir, app_name, conv_id) across both
    Antigravity Hub (~/.gemini/antigravity/brain) and Antigravity IDE (~/.gemini/antigravity-ide/brain).
    """
    # 1. If an explicit existing file path was passed
    if conv_or_path and os.path.isfile(conv_or_path):
        t_path = os.path.abspath(conv_or_path)
        conv_root = os.path.dirname(os.path.dirname(os.path.dirname(t_path)))
        u_dir = os.path.join(conv_root, '.user_uploaded')
        conv_id = os.path.basename(conv_root)
        app_name = 'Antigravity IDE' if 'antigravity-ide' in t_path.lower() else 'Antigravity Hub'
        return t_path, u_dir, app_name, conv_id

    # 2. If a directory path was passed
    if conv_or_path and os.path.isdir(conv_or_path):
        conv_root = os.path.abspath(conv_or_path)
        t_full = os.path.join(conv_root, '.system_generated', 'logs', 'transcript_full.jsonl')
        t_compact = os.path.join(conv_root, '.system_generated', 'logs', 'transcript.jsonl')
        t_path = t_full if os.path.exists(t_full) else t_compact
        u_dir = os.path.join(conv_root, '.user_uploaded')
        conv_id = os.path.basename(conv_root)
        app_name = 'Antigravity IDE' if 'antigravity-ide' in conv_root.lower() else 'Antigravity Hub'
        return t_path, u_dir, app_name, conv_id

    # 3. Check environment variable if no explicit parameter was passed
    if not conv_or_path:
        env_conv = os.environ.get('CONVERSATION_ID') or os.environ.get('AG_CONVERSATION_ID')
        if env_conv:
            conv_or_path = env_conv

    # 4. If 'latest' was requested (or fallback if default not found), scan both brain directories
    if conv_or_path == 'latest':
        candidates = []
        for env_key, b_dir in BRAIN_DIRS.items():
            if prefer_env and prefer_env != env_key:
                continue
            if os.path.isdir(b_dir):
                for entry in os.listdir(b_dir):
                    c_root = os.path.join(b_dir, entry)
                    t_full = os.path.join(c_root, '.system_generated', 'logs', 'transcript_full.jsonl')
                    t_compact = os.path.join(c_root, '.system_generated', 'logs', 'transcript.jsonl')
                    t_file = t_full if os.path.exists(t_full) else (t_compact if os.path.exists(t_compact) else None)
                    if t_file:
                        candidates.append((os.path.getmtime(t_file), t_file, os.path.join(c_root, '.user_uploaded'),
                                           'Antigravity IDE' if env_key == 'ag_ide' else 'Antigravity Hub', entry))
        if candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            _, t_path, u_dir, app_name, conv_id = candidates[0]
            return t_path, u_dir, app_name, conv_id

    # 5. Look up by conversation ID in both Antigravity Hub and Antigravity IDE
    target_id = conv_or_path or DEFAULT_CONV_ID
    if target_id == 'current':
        target_id = DEFAULT_CONV_ID

    search_order = ['ag_hub', 'ag_ide'] if prefer_env != 'ag_ide' else ['ag_ide', 'ag_hub']
    for env_key in search_order:
        b_dir = BRAIN_DIRS[env_key]
        c_root = os.path.join(b_dir, target_id)
        t_full = os.path.join(c_root, '.system_generated', 'logs', 'transcript_full.jsonl')
        t_compact = os.path.join(c_root, '.system_generated', 'logs', 'transcript.jsonl')
        if os.path.exists(t_full) or os.path.exists(t_compact):
            t_path = t_full if os.path.exists(t_full) else t_compact
            u_dir = os.path.join(c_root, '.user_uploaded')
            app_name = 'Antigravity IDE' if env_key == 'ag_ide' else 'Antigravity Hub'
            return t_path, u_dir, app_name, target_id

    # 6. Fallback to latest if default target_id wasn't found
    candidates = []
    for env_key, b_dir in BRAIN_DIRS.items():
        if os.path.isdir(b_dir):
            for entry in os.listdir(b_dir):
                c_root = os.path.join(b_dir, entry)
                t_full = os.path.join(c_root, '.system_generated', 'logs', 'transcript_full.jsonl')
                t_compact = os.path.join(c_root, '.system_generated', 'logs', 'transcript.jsonl')
                t_file = t_full if os.path.exists(t_full) else (t_compact if os.path.exists(t_compact) else None)
                if t_file:
                    candidates.append((os.path.getmtime(t_file), t_file, os.path.join(c_root, '.user_uploaded'),
                                       'Antigravity IDE' if env_key == 'ag_ide' else 'Antigravity Hub', entry))
    if candidates:
        candidates.sort(key=lambda x: x[0], reverse=True)
        _, t_path, u_dir, app_name, conv_id = candidates[0]
        print(f"[Notice] Requested '{target_id}' not found; automatically fell back to latest session '{conv_id}' ({app_name}).")
        return t_path, u_dir, app_name, conv_id

    raise FileNotFoundError(
        f"Could not find transcript for '{target_id}' in Antigravity Hub ({BRAIN_DIRS['ag_hub']}) "
        f"or Antigravity IDE ({BRAIN_DIRS['ag_ide']})."
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Universal Chat History HTML Builder for AstroMatch Pro (Antigravity Hub & IDE)"
    )
    parser.add_argument('positional_target', nargs='?', default=None,
                        help="Conversation ID, transcript path, 'current', or 'latest'")
    parser.add_argument('positional_upload_dir', nargs='?', default=None,
                        help="Optional explicit user_uploaded directory path")
    parser.add_argument('--conv', '-c', dest='conv', default=None,
                        help="Conversation ID, directory path, 'current', or 'latest'")
    parser.add_argument('--env', '-e', dest='env', choices=['ag_hub', 'ag_ide'], default=None,
                        help="Prefer 'ag_hub' (Antigravity Hub) or 'ag_ide' (Antigravity IDE)")
    parser.add_argument('--out', '-o', dest='out', default=None,
                        help="Output HTML filename (default: chat_history_astromatch_v250.html)")
    parser.add_argument('--no-portal-update', action='store_true',
                        help="Skip updating chat_transcripts.html portal")
    return parser.parse_args()


args = parse_args()
target_spec = args.conv or args.positional_target or DEFAULT_CONV_ID

transcript_path, user_upload_dir, app_environment, conversation_id = resolve_conversation_paths(
    target_spec, prefer_env=args.env
)
if args.positional_upload_dir and os.path.exists(args.positional_upload_dir):
    user_upload_dir = args.positional_upload_dir

short_id = conversation_id[:8]
sess_meta = SESSION_METADATA.get(short_id, {})

if args.out:
    output_filename = os.path.basename(args.out)
else:
    output_filename = sess_meta.get('filename', f"chat_astromatch_session_{short_id}.html")

output_path_root = os.path.join(ROOT_DIR, output_filename)
output_path_exports = os.path.join(ROOT_DIR, 'chat_exports', output_filename)
named_export_file = output_filename
portal_card_title = sess_meta.get(
    'title',
    f"AstroMatch Pro v2.5.0 Expert Astrologist Session ({html.escape(app_environment)} - {html.escape(short_id)})"
)
output_path_named = os.path.join(ROOT_DIR, 'chat_exports', named_export_file)

steps = []
with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                steps.append(json.loads(line))
            except Exception:
                pass

print(f"[{app_environment}] Loaded {len(steps)} steps from: {transcript_path}")

# Load all user uploaded images with their timestamps
user_images = []
if os.path.exists(user_upload_dir):
    for fname in os.listdir(user_upload_dir):
        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            fpath = os.path.join(user_upload_dir, fname)
            mtime = os.path.getmtime(fpath)
            file_ts = mtime
            match = re.search(r'media_(\d+)', fname)
            if match:
                try:
                    file_ts = int(match.group(1)) / 1000.0
                except Exception:
                    pass
            user_images.append({
                'name': fname,
                'path': fpath,
                'timestamp': file_ts
            })

user_images.sort(key=lambda x: x['timestamp'])
print(f"Loaded {len(user_images)} user uploaded screenshots from {user_upload_dir}.")


def find_images_for_turn(turn_iso_time, u_step=None):
    matched = []
    seen_paths = set()

    # 1. Check direct media array on the step
    if u_step and isinstance(u_step.get('media'), list):
        for m in u_step['media']:
            uri = m.get('uri', '')
            if uri.startswith('file:///'):
                uri_path = uri.replace('file:///', '').replace('/', os.sep)
            else:
                uri_path = uri
            if uri_path and os.path.exists(uri_path) and uri_path not in seen_paths:
                seen_paths.add(uri_path)
                matched.append({
                    'name': os.path.basename(uri_path),
                    'path': uri_path,
                    'timestamp': 0
                })

    # 2. Check timestamp proximity in .user_uploaded directory
    if turn_iso_time and user_images:
        try:
            clean_time = turn_iso_time.replace('Z', '+00:00')
            turn_dt = datetime.datetime.fromisoformat(clean_time)
            turn_ts = turn_dt.timestamp()
            for img in user_images:
                diff = abs(img['timestamp'] - turn_ts)
                if diff <= 300 and img['path'] not in seen_paths:
                    seen_paths.add(img['path'])
                    matched.append(img)
        except Exception:
            pass

    return matched


def extract_model_from_settings(content_text):
    """
    Parses <USER_SETTINGS_CHANGE> blocks for Model Selection changes.
    """
    if not content_text or '<USER_SETTINGS_CHANGE>' not in content_text:
        return None
    try:
        settings_block = content_text.split('<USER_SETTINGS_CHANGE>')[1].split('</USER_SETTINGS_CHANGE>')[0]
        pattern = r'Model Selection`?\s+from\s+[^\r\n]*?\bto\s+([A-Z][A-Za-z0-9.\s\-_]+?\([A-Za-z0-9\s]+\)|[A-Z][A-Za-z0-9.\-_]+)'
        m = re.search(pattern, settings_block)
        if m:
            clean_name = m.group(1).strip()
            if len(clean_name) <= 60:
                return clean_name
    except Exception:
        pass
    return None


# Pre-scan steps for initial model selection if present
active_model = "Gemini 4 Argon (Medium)" if app_environment == 'Antigravity Hub' else "Gemini 3.8 Flash (High)"
for s in steps:
    if s.get('type') == 'USER_INPUT':
        detected = extract_model_from_settings(s.get('content', ''))
        if detected:
            active_model = detected
            break

# Group steps into conversation turns
turns = []
current_turn = None
models_used_set = []

for s in steps:
    stype = s.get('type')
    content = s.get('content', '')

    if stype == 'USER_INPUT':
        new_model = extract_model_from_settings(content)
        if new_model:
            active_model = new_model

        if active_model not in models_used_set:
            models_used_set.append(active_model)

        if current_turn:
            turns.append(current_turn)
        current_turn = {
            'user_step': s,
            'model': active_model,
            'app': app_environment,
            'assistant_steps': []
        }
    else:
        if current_turn:
            current_turn['model'] = active_model
            current_turn['assistant_steps'].append(s)

if current_turn:
    turns.append(current_turn)

print(f"Extracted {len(turns)} conversation turns. Models detected: {models_used_set}")


def get_model_badge_classes(model_name):
    m_lower = model_name.lower()
    if 'argon' in m_lower or 'gemini 4' in m_lower:
        return 'badge-argon', 'tag-argon', 'model-pill-argon'
    elif 'flash' in m_lower:
        return 'badge-flash', 'tag-flash', 'model-pill-flash'
    return 'badge-pro', 'tag-pro', 'model-pill-pro'


def format_text(text):
    if not text:
        return ""
    escaped = html.escape(text)
    # Code blocks
    escaped = re.sub(
        r'```([a-zA-Z0-9_-]*)\n(.*?)```',
        r'<pre><code class="language-\1">\2</code></pre>',
        escaped,
        flags=re.DOTALL
    )
    # Inline code
    escaped = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', escaped)
    # Bold
    escaped = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', escaped)
    # Italic
    escaped = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', escaped)
    # Links
    escaped = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', escaped)
    # Paragraphs and line breaks
    escaped = escaped.replace('\n\n', '</p><p>').replace('\n', '<br>')
    return f"<p>{escaped}</p>"


def get_base64_image(img_path):
    try:
        if not os.path.exists(img_path):
            return ""
        ext = os.path.splitext(img_path)[1].lower().replace('.', '')
        mime = 'image/png' if ext == 'png' else ('image/jpeg' if ext in ['jpg', 'jpeg'] else 'image/webp')
        with open(img_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        return f"data:{mime};base64,{b64}"
    except Exception:
        return ""


html_turns = []

for idx, turn in enumerate(turns):
    u_step = turn['user_step']
    u_content = u_step.get('content', '')
    u_time = u_step.get('created_at', '')
    model_name = turn['model']
    app_name = turn['app']
    badge_cls, tag_cls, pill_cls = get_model_badge_classes(model_name)

    # Extract user text cleanly
    user_req = u_content
    settings_text = ""
    metadata_text = ""

    if '<USER_SETTINGS_CHANGE>' in user_req:
        try:
            settings_text = user_req.split('<USER_SETTINGS_CHANGE>')[1].split('</USER_SETTINGS_CHANGE>')[0].strip()
            user_req = user_req.split('<USER_SETTINGS_CHANGE>')[0] + user_req.split('</USER_SETTINGS_CHANGE>')[1]
        except Exception:
            pass

    if '<ADDITIONAL_METADATA>' in user_req:
        try:
            metadata_text = user_req.split('<ADDITIONAL_METADATA>')[1].split('</ADDITIONAL_METADATA>')[0].strip()
            user_req = user_req.split('<ADDITIONAL_METADATA>')[0] + user_req.split('</ADDITIONAL_METADATA>')[1]
        except Exception:
            pass

    if '<USER_REQUEST>' in user_req:
        try:
            user_req = user_req.split('<USER_REQUEST>')[1].split('</USER_REQUEST>')[0]
        except Exception:
            pass

    user_req = user_req.strip()

    # Look for attached images
    attached_images = find_images_for_turn(u_time, u_step)
    images_html = ""
    if attached_images:
        images_html = '<div class="attached-images-grid">'
        for img in attached_images:
            b64 = get_base64_image(img['path'])
            if b64:
                images_html += f"""
                <div class="image-card">
                  <a href="{b64}" target="_blank" title="Click to view full image">
                    <img src="{b64}" alt="{html.escape(img['name'])}" loading="lazy">
                  </a>
                  <span class="img-caption">{html.escape(img['name'])}</span>
                </div>
                """
        images_html += '</div>'

    # Collect assistant output
    responses = []
    thoughts = []
    tool_calls_list = []

    for a_step in turn['assistant_steps']:
        # Thinking
        th = a_step.get('thinking', '')
        if th:
            thoughts.append(th)

        # Content text
        txt = a_step.get('content', '')
        if txt and not a_step.get('tool_calls'):
            responses.append(txt)

        # Tool calls
        if a_step.get('tool_calls'):
            t_calls = a_step.get('tool_calls', [])
            for tc in t_calls:
                tool_calls_list.append(tc)

    # Format timestamp nicely
    ts_display = u_time[:19].replace('T', ' ') if u_time else ''

    # Build turn HTML
    turn_html = f"""
    <div class="chat-turn" id="turn-{idx+1}">
      <div class="turn-header">
        <div class="turn-header-left">
          <span class="turn-pill">Turn #{idx+1}</span>
          <span class="timestamp-label">⏰ {ts_display} UTC</span>
        </div>
        <div class="turn-header-right">
          <span class="model-badge {badge_cls}">🤖 {html.escape(model_name)}</span>
          <span class="env-tag">{html.escape(app_name)}</span>
        </div>
      </div>

      <div class="message-block user-block">
        <div class="message-sender">
          <span class="sender-avatar">👤</span>
          <span class="sender-title">User Prompt</span>
        </div>
        <div class="message-body">
          {format_text(user_req)}
          {images_html}
        </div>
    """

    if settings_text:
        turn_html += f"""
        <details class="settings-details">
          <summary>⚙️ User Settings Change</summary>
          <pre>{html.escape(settings_text)}</pre>
        </details>
        """

    if metadata_text:
        turn_html += f"""
        <details class="metadata-details">
          <summary>ℹ️ Additional Session Metadata</summary>
          <pre>{html.escape(metadata_text)}</pre>
        </details>
        """

    turn_html += """
      </div>
    """

    # Assistant Response Section
    if responses or thoughts or tool_calls_list:
        combined_response = "\n\n".join(responses) if responses else ""
        turn_html += f"""
      <div class="message-block assistant-block">
        <div class="message-sender">
          <span class="sender-avatar">⚡</span>
          <div class="sender-info">
            <span class="sender-title">Antigravity Agent</span>
            <span class="model-subtag {tag_cls}">{html.escape(model_name)}</span>
          </div>
        </div>
        """

        if thoughts:
            combined_thoughts = "\n\n---\n\n".join(thoughts)
            turn_html += f"""
        <details class="thoughts-details">
          <summary>💭 Agent Thinking &amp; Reasoning Process ({len(thoughts)} thought blocks)</summary>
          <div class="thoughts-text">{format_text(combined_thoughts)}</div>
        </details>
            """

        if tool_calls_list:
            turn_html += f"""
        <details class="tool-calls-details">
          <summary>🛠️ Executed Tool Actions ({len(tool_calls_list)} actions)</summary>
          <div class="tool-calls-content">
            """
            for tc in tool_calls_list:
                tc_name = tc.get('name', 'tool')
                tc_args = json.dumps(tc.get('args', {}), indent=2, ensure_ascii=False)
                turn_html += f"""
            <div class="tool-call-item">
              <div class="tool-name"><code>{html.escape(tc_name)}</code></div>
              <pre class="tool-args">{html.escape(tc_args)}</pre>
            </div>
                """
            turn_html += """
          </div>
        </details>
            """

        if combined_response:
            turn_html += f"""
        <div class="message-body assistant-body">
          {format_text(combined_response)}
        </div>
            """

        turn_html += """
      </div>
        """

    turn_html += """
    </div>
    """
    html_turns.append(turn_html)

total_turns = len(turns)
total_steps_count = len(steps)
date_start = steps[0].get('created_at', '')[:10] if steps else ''
date_end = steps[-1].get('created_at', '')[:10] if steps else ''
date_range_str = date_start if date_start == date_end else f"{date_start} to {date_end}"

model_pills_html = ""
for m_name in models_used_set:
    b_cls, t_cls, pill_cls = get_model_badge_classes(m_name)
    icon = "🧬" if "Argon" in m_name else ("⚡" if "Flash" in m_name else "🤖")
    model_pills_html += f'<div class="stat-pill {pill_cls}">{icon} {html.escape(m_name)}</div>\n        '

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AstroMatch Pro - Development Chat History ({html.escape(app_environment)})</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-primary: #070913;
      --bg-secondary: #0f172a;
      --bg-tertiary: #1e293b;
      --bg-card: rgba(17, 24, 43, 0.92);
      --accent-purple: #c084fc;
      --accent-blue: #38bdf8;
      --accent-cyan: #22d3ee;
      --accent-green: #10b981;
      --accent-amber: #fbbf24;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-subtle: #64748b;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(251, 191, 36, 0.35);
      --font-sans: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg-primary);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding: 0;
      margin: 0;
    }}
    .header-banner {{
      background: linear-gradient(180deg, #0d1326 0%, var(--bg-primary) 100%);
      border-bottom: 1px solid var(--border-color);
      padding: 32px 24px 20px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }}
    .header-content {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .header-title-box h1 {{
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 4px;
    }}
    .stats-badges {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
    }}
    .stat-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 4px 12px;
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--text-muted);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .stat-pill strong {{ color: var(--text-main); }}
    .model-pill-argon {{
      background: rgba(168, 85, 247, 0.15);
      border-color: rgba(168, 85, 247, 0.4);
      color: #d8b4fe;
    }}
    .model-pill-flash {{
      background: rgba(245, 158, 11, 0.15);
      border-color: rgba(245, 158, 11, 0.4);
      color: #fcd34d;
    }}
    .model-pill-pro {{
      background: rgba(59, 130, 246, 0.15);
      border-color: rgba(59, 130, 246, 0.4);
      color: #93c5fd;
    }}
    .env-pill {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
    }}
    .search-filter-bar {{
      max-width: 1200px;
      margin: 16px auto 0;
    }}
    .search-input {{
      width: 100%;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 10px 16px;
      font-family: var(--font-sans);
      font-size: 0.92rem;
      color: var(--text-main);
      outline: none;
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--accent-amber);
      background: rgba(255, 255, 255, 0.07);
      box-shadow: 0 0 15px rgba(251, 191, 36, 0.25);
    }}
    .main-chat-container {{
      max-width: 1200px;
      margin: 24px auto 80px;
      padding: 0 20px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .chat-turn {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
      transition: border-color 0.2s;
    }}
    .chat-turn:hover {{
      border-color: var(--border-hover);
    }}
    .turn-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 14px;
      margin-bottom: 18px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }}
    .turn-header-left, .turn-header-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .turn-pill {{
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.2), rgba(245, 158, 11, 0.2));
      border: 1px solid rgba(251, 191, 36, 0.4);
      color: var(--accent-amber);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
    }}
    .timestamp-label {{
      font-size: 0.78rem;
      color: var(--text-subtle);
    }}
    .model-badge {{
      font-size: 0.8rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 12px;
      border: 1px solid transparent;
    }}
    .badge-argon {{
      background: rgba(168, 85, 247, 0.2);
      color: #c084fc;
      border-color: rgba(168, 85, 247, 0.4);
    }}
    .badge-flash {{
      background: rgba(245, 158, 11, 0.2);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.4);
    }}
    .badge-pro {{
      background: rgba(59, 130, 246, 0.2);
      color: #60a5fa;
      border-color: rgba(59, 130, 246, 0.4);
    }}
    .env-tag {{
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      font-size: 0.75rem;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .message-block {{
      margin-bottom: 16px;
    }}
    .message-sender {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .sender-avatar {{
      font-size: 1.2rem;
    }}
    .sender-title {{
      font-weight: 600;
      font-size: 0.95rem;
      color: var(--text-main);
    }}
    .model-subtag {{
      font-size: 0.7rem;
      padding: 1px 6px;
      border-radius: 4px;
      margin-left: 6px;
    }}
    .tag-argon {{ background: rgba(168, 85, 247, 0.2); color: #d8b4fe; }}
    .tag-flash {{ background: rgba(245, 158, 11, 0.2); color: #fde68a; }}
    .tag-pro {{ background: rgba(59, 130, 246, 0.2); color: #bfdbfe; }}

    .message-body {{
      font-size: 0.95rem;
      color: #e2e8f0;
      line-height: 1.7;
      word-break: break-word;
    }}
    .message-body p {{ margin-bottom: 12px; }}
    .message-body code {{
      background: rgba(0, 0, 0, 0.4);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: #fbcfe8;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .message-body pre {{
      background: #090d1a;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 14px;
      overflow-x: auto;
      margin: 12px 0;
    }}
    .message-body pre code {{
      background: transparent;
      padding: 0;
      border: none;
      color: #e2e8f0;
    }}
    .message-body a {{
      color: var(--accent-blue);
      text-decoration: underline;
    }}

    .user-block {{
      background: rgba(56, 189, 248, 0.04);
      border: 1px solid rgba(56, 189, 248, 0.15);
      border-radius: 10px;
      padding: 16px;
      margin-bottom: 20px;
    }}
    .assistant-block {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 16px;
    }}

    details summary {{
      cursor: pointer;
      font-size: 0.85rem;
      color: var(--text-muted);
      padding: 6px 10px;
      background: rgba(255, 255, 255, 0.03);
      border-radius: 6px;
      margin: 10px 0;
      user-select: none;
      transition: background 0.2s;
    }}
    details summary:hover {{
      background: rgba(255, 255, 255, 0.07);
      color: var(--text-main);
    }}
    .thoughts-text {{
      font-size: 0.88rem;
      color: #94a3b8;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 14px;
      margin-top: 8px;
      line-height: 1.6;
    }}
    .tool-calls-content {{
      margin-top: 8px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .tool-call-item {{
      background: #090d1a;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      padding: 10px;
    }}
    .tool-name code {{
      color: var(--accent-amber);
      font-weight: 600;
    }}
    .tool-args {{
      font-size: 0.82rem;
      color: #cbd5e1;
      margin-top: 6px;
      max-height: 250px;
      overflow-y: auto;
    }}
    .settings-details pre, .metadata-details pre {{
      font-size: 0.82rem;
      color: #94a3b8;
      padding: 8px;
      background: #090d1a;
      border-radius: 6px;
      margin-top: 6px;
      white-space: pre-wrap;
    }}
    .attached-images-grid {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 12px;
    }}
    .image-card {{
      max-width: 320px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
      background: #000;
    }}
    .image-card img {{
      width: 100%;
      height: auto;
      display: block;
    }}
    .img-caption {{
      display: block;
      font-size: 0.72rem;
      color: var(--text-subtle);
      padding: 4px 8px;
      text-align: center;
      background: #090d1a;
    }}
  </style>
</head>
<body>

  <header class="header-banner">
    <div class="header-content">
      <div class="header-title-box">
        <h1>🔮 AstroMatch Pro - Development Chat History ({html.escape(app_environment)})</h1>
        <div class="header-subtitle">Chronological export of v2.5.0 Expert Astrologist Engine, Blind Portrait mode, Current Date Transits, and Elon Musk Verification (Session <code>{html.escape(conversation_id[:8])}</code>)</div>
      </div>
      <div class="stats-badges">
        <div class="stat-pill">💬 Turns: <strong>{total_turns}</strong></div>
        <div class="stat-pill">⚙️ Trajectory Steps: <strong>{total_steps_count}</strong></div>
        <div class="stat-pill">📅 Date: <strong>{html.escape(date_range_str)}</strong></div>
        <div class="stat-pill env-pill">🛠️ {html.escape(app_environment)}</div>
        {model_pills_html.strip()}
      </div>
    </div>
    <div class="search-filter-bar">
      <input type="text" class="search-input" id="chatSearchInput" placeholder="🔍 Search chat history (e.g. 'Elon Musk', 'אופק', 'Blind Mode', 'Transits', 'v2.5.0', 'SpaceX', 'Porphyry')...">
    </div>
  </header>

  <main class="main-chat-container" id="chatTurnsContainer">
    {''.join(html_turns)}
  </main>

  <script>
    const searchInput = document.getElementById('chatSearchInput');
    const turns = document.querySelectorAll('.chat-turn');

    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.toLowerCase().trim();
      turns.forEach(turn => {{
        if (!query) {{
          turn.style.display = 'block';
        }} else {{
          const text = turn.innerText.toLowerCase();
          turn.style.display = text.includes(query) ? 'block' : 'none';
        }}
      }});
    }});
  </script>

</body>
</html>
"""

# Write root output file
with open(output_path_root, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f"Generated {output_path_root} ({len(full_html):,} bytes)")

# Also write a standard named file for convenience
standard_named_root = os.path.join(ROOT_DIR, "chat_history_astromatch_v250.html")
with open(standard_named_root, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f"Generated {standard_named_root} ({len(full_html):,} bytes)")

# Write chat_exports output files if directory exists
if os.path.exists(os.path.join(ROOT_DIR, 'chat_exports')):
    with open(output_path_exports, 'w', encoding='utf-8') as f:
        f.write(full_html)
    with open(output_path_named, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {output_path_exports} ({len(full_html):,} bytes)")
    print(f"Generated {output_path_named} ({len(full_html):,} bytes)")


# Update chat_transcripts.html and chat_exports/index.html portal cards if present
def update_portal(portal_path, relative_link):
    if not os.path.exists(portal_path):
        return
    with open(portal_path, 'r', encoding='utf-8') as pf:
        p_html = pf.read()

    card_html = f"""        <div class="session-card">
            <div class="card-header">
                <h3><a href="{relative_link}">{portal_card_title}</a></h3>
                <span class="badge">{total_turns} Prompts</span>
            </div>
            <div class="card-meta">
                <span><i class="fas fa-calendar-alt"></i> {date_range_str}</span>
                <span><i class="fas fa-fingerprint"></i> <code>{conversation_id}</code></span>
            </div>
            <div class="card-actions">
                <a href="{relative_link}" class="view-btn"><i class="fas fa-eye"></i> View Full Chat</a>
                <span class="raw-steps">{total_steps_count} log steps</span>
            </div>
        </div>"""

    # If this conversation is already present, update its card in-place
    existing_pattern = re.compile(
        r'[ \t]*<div class="session-card">\s*<div class="card-header">.*?<code>'
        + re.escape(conversation_id)
        + r'</code>.*?</div>\s*</div>',
        re.DOTALL
    )
    if existing_pattern.search(p_html):
        p_html = existing_pattern.sub(card_html, p_html, count=1)
        with open(portal_path, 'w', encoding='utf-8') as pf:
            pf.write(p_html)
        print(f"Updated existing card in portal: {portal_path}")
        return

    if '<div class="sessions-grid">' in p_html:
        p_html = p_html.replace('<div class="sessions-grid">', '<div class="sessions-grid">\n\n' + card_html + '\n')
        with open(portal_path, 'w', encoding='utf-8') as pf:
            pf.write(p_html)
        print(f"Added new card to portal: {portal_path}")


if not args.no_portal_update:
    update_portal(os.path.join(ROOT_DIR, 'chat_transcripts.html'), output_filename)
    update_portal(os.path.join(ROOT_DIR, 'chat_exports', 'index.html'), output_filename)

print(f"Done! AstroMatch Pro chat history files generated successfully.")
