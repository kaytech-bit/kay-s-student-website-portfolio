"""Generates the static HTML pages. Run: python3 build.py  (output is plain HTML, no build step needed to host)."""
PAGES = [("index.html", "Home"), ("about.html", "About"), ("skills.html", "Skills"),
         ("projects.html", "Projects"), ("academics.html", "Academics"),
         ("planner.html", "Planner"), ("contact.html", "Contact")]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title} | Clement Idongesit Sunday</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html">Clement<span>.</span></a>
    <nav class="nav" id="nav" aria-label="Main">
{links}
    </nav>
    <button class="theme-toggle" type="button" aria-label="Switch light or dark theme">🌓</button>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="container footer-inner">
    <span>© <span id="year">2026</span> Clement Idongesit Sunday. Miva University, Computer Science.</span>
    <span><a href="https://github.com/kaytech-bit" rel="noopener">GitHub</a> · <a href="contact.html">Contact</a></span>
  </div>
</footer>
<script src="js/main.js"></script>
{extra}</body>
</html>
"""


def page(fname, title, desc, body, extra=""):
    links = "\n".join(
        '      <a href="%s"%s>%s</a>' % (f, ' class="active" aria-current="page"' if f == fname else "", n)
        for f, n in PAGES)
    html = HEAD.format(title=title, desc=desc, links=links) + body + FOOT.format(extra=extra)
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(html)


def head(h, sub):
    return '<section class="page-head"><div class="container"><h1>%s</h1><p>%s</p></div></section>\n' % (h, sub)


# ---------------- Home ----------------
page("index.html", "Home", "Portfolio of Clement Idongesit Sunday, Computer Science student at Miva University and network analyst.", """
<section class="container hero">
  <div class="hero-text">
    <p class="hello">Hello, I'm</p>
    <h1>Clement Idongesit Sunday</h1>
    <p class="welcome">Welcome to my world. <em>Everything is possible, technically.</em></p>
    <p class="bio">I'm a Computer Science student at Miva University (100 Level) and a network analyst. I learn by reading logs, tracing traffic and building things that work.</p>
    <div class="actions">
      <a class="btn primary" href="projects.html">See my projects</a>
      <a class="btn" href="contact.html">Get in touch</a>
    </div>
  </div>
  <div class="hero-photo">
    <img src="images/clement.jpg" alt="Clement Idongesit Sunday smiling, wearing a brown pinstriped top with gold piping" width="802" height="1080">
  </div>
</section>

<section class="section">
  <div class="container grid cols-3">
    <div class="panel gold"><h3>About me</h3><p>My background, interests and what I'm working towards.</p><a class="more" href="about.html">Read my story</a></div>
    <div class="panel gold"><h3>Skills</h3><p>Splunk, Wireshark, Linux and the other tools I use daily.</p><a class="more" href="skills.html">View skills</a></div>
    <div class="panel gold"><h3>Academic planner</h3><p>Add tasks, tick them off and work out your CGPA. Built by me.</p><a class="more" href="planner.html">Open the planner</a></div>
  </div>
</section>
""")

# ---------------- About ----------------
page("about.html", "About", "About Clement Idongesit Sunday: education, career aspirations, technical skills, hobbies and interests.",
     head("About me", "A computer science student who likes seeing what the network is really doing.") + """
<section class="section">
  <div class="container grid cols-2">
    <article>
      <h2>My story</h2>
      <p>I'm Clement, a Computer Science student at Miva University and a network analyst. I got into cybersecurity by wanting to understand what happens between one machine and another, and I haven't stopped asking that question since.</p>
      <p>My motto is on the homepage for a reason: everything is possible, technically. You just have to find the technical way.</p>
    </article>
    <aside class="panel leaf">
      <h3>Quick facts</h3>
      <dl class="facts">
        <dt>Name</dt><dd>Clement Idongesit Sunday</dd>
        <dt>University</dt><dd>Miva University</dd>
        <dt>Programme</dt><dd>BSc Computer Science</dd>
        <dt>Level</dt><dd>100 Level</dd>
        <dt>Expected</dt><dd>2029</dd>
        <dt>Role</dt><dd>Network analyst</dd>
      </dl>
    </aside>
  </div>
</section>

<section class="section alt">
  <div class="container grid cols-2">
    <article>
      <h2>Educational background</h2>
      <ul>
        <li><strong>BSc Computer Science</strong>, Miva University (2025 to 2029, currently 100 Level)</li>
        <li><strong>Networking Basics</strong>, Cisco Networking Academy (November 2026)</li>
        <li><strong>Cybersecurity certification</strong>, TS Academy</li>
        <li><strong>Project Management certifications</strong>, Google</li>
      </ul>
    </article>
    <article>
      <h2>Career aspirations</h2>
      <p>I want to work as a remote SOC analyst, watching for threats and responding to incidents for teams anywhere in the world. Over the longer term I want to grow into threat detection and security engineering, and use what I learn to help more Africans get into cybersecurity.</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="container grid cols-2">
    <article>
      <h2>Technical skills</h2>
      <ul class="tags">
        <li>Splunk SIEM</li><li>SPL</li><li>Wireshark</li><li>Linux</li><li>Windows Event Logs</li>
        <li>MITRE ATT&amp;CK</li><li>HTML</li><li>CSS</li><li>JavaScript</li><li>Project management</li>
      </ul>
      <p><a href="skills.html">See skill levels</a></p>
    </article>
    <article>
      <h2>Hobbies and interests</h2>
      <ul>
        <li><strong>Football:</strong> I support Portugal and France.</li>
        <li><strong>Web3 and African tech:</strong> following how the ecosystem grows and how security fits in.</li>
        <li><strong>Learning security:</strong> labs, log hunting and capture-the-flag style practice.</li>
      </ul>
    </article>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Meet me</h2>
    <figure class="video">
      <video controls preload="metadata" poster="images/video-poster.jpg" width="1280" height="720">
        <source src="media/intro.mp4" type="video/mp4">
        Your browser does not support video. <a href="media/intro.mp4">Download the intro video</a>.
      </video>
      <figcaption>A short introduction.</figcaption>
    </figure>
  </div>
</section>
""")

# ---------------- Skills ----------------
def skill(name, lvl):
    return ('<div class="skill"><div class="skill-top"><span>%s</span><span>%d%%</span></div>'
            '<div class="bar" role="img" aria-label="%s: %d percent"><i data-level="%d"></i></div></div>' % (name, lvl, name, lvl, lvl))

page("skills.html", "Skills", "Technical skills of Clement Idongesit Sunday: Splunk, SPL, Wireshark, Linux, MITRE ATT&CK, and more.",
     head("Skills", "What I can do today, and what I'm still sharpening.") + """
<section class="section">
  <div class="container grid cols-2">
    <div>
      <h2>Security and networking</h2>
""" + skill("Splunk SIEM and SPL", 80) + skill("Wireshark packet analysis", 80) + skill("Windows Event Logs", 75)
     + skill("Linux command line", 75) + skill("MITRE ATT&amp;CK mapping", 70) + """
    </div>
    <div>
      <h2>Web and project skills</h2>
""" + skill("HTML and CSS", 70) + skill("JavaScript", 55) + skill("Project management", 70) + """
      <h3 style="margin-top:2rem">Tools I use</h3>
      <ul class="tags">
        <li>Splunk</li><li>SPL</li><li>Wireshark</li><li>Linux</li><li>Windows Event Logs</li>
        <li>MITRE ATT&amp;CK</li><li>Git and GitHub</li><li>Google Workspace</li>
      </ul>
    </div>
  </div>
</section>
""")

# ---------------- Projects ----------------
def project(cat, title, stack, text, img, alt, link=""):
    return ('<article class="panel project" data-cat="%s"><figure><img src="images/%s" alt="%s" width="800" height="500" loading="lazy"></figure>'
            '<h3>%s</h3><p class="stack">%s</p><p>%s</p><div class="links">%s</div></article>' % (cat, img, alt, title, stack, text, link))

page("projects.html", "Projects", "Projects by Clement Idongesit Sunday in security analysis, networking and web development.",
     head("Projects", "Hands-on work in log analysis, traffic analysis and the web.") + """
<section class="section">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter projects">
      <button class="chip on" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="chip" type="button" data-filter="security" aria-pressed="false">Security</button>
      <button class="chip" type="button" data-filter="web" aria-pressed="false">Web</button>
    </div>
    <div class="grid cols-3">
""" + project("security", "Splunk log investigation", "Splunk · SPL · Windows Event Logs",
              "Searched Windows event data with SPL to spot failed logins and suspicious activity, then mapped the findings to MITRE ATT&amp;CK.",
              "project-splunk.svg", "Splunk dashboard charting failed logins by hour with a spike at 4 a.m.",
              '<a href="#">Write-up (coming soon)</a>')
     + project("security", "Network traffic analysis", "Wireshark · Linux",
               "Captured and inspected packets to follow a connection from handshake to teardown and flag traffic that looked wrong.",
               "project-wireshark.svg", "Wireshark packet list showing a TCP handshake followed by an HTTP request",
               '<a href="#">Write-up (coming soon)</a>')
     + project("web", "Student portfolio and academic planner", "HTML · CSS · JavaScript",
               "This website. A responsive multi-page portfolio with a task planner and CGPA calculator that save data in your browser.",
               "project-portfolio.svg", "Homepage of this portfolio website with a task list below the introduction",
               '<a href="index.html">View the site</a> <a href="https://github.com/kaytech-bit/kay-s-student-website" rel="noopener">Source code</a>') + """
    </div>
  </div>
</section>
""")

# ---------------- Academics ----------------
page("academics.html", "Academics", "Education, certifications and academic goals of Clement Idongesit Sunday.",
     head("Academics", "Where I'm studying and what I've already completed.") + """
<section class="section">
  <div class="container grid cols-2">
    <div>
      <h2>Education and certifications</h2>
      <ol class="timeline">
        <li><h3>BSc Computer Science, Miva University</h3><p class="when">Started 2025 · Expected 2029 · Currently 100 Level</p><p>Building a foundation in programming, networks and computing theory.</p></li>
        <li><h3>Networking Basics, Cisco Networking Academy</h3><p class="when">10 November 2026</p><p>Core networking concepts: how devices connect, address and talk to each other.</p></li>
        <li><h3>Cybersecurity certification, TS Academy</h3><p>Practical training in security monitoring and incident analysis.</p></li>
        <li><h3>Project Management certifications, Google</h3><p>Planning, scheduling and delivering projects with clear goals.</p></li>
      </ol>
    </div>
    <div>
      <h2>Academic goals</h2>
      <div class="panel leaf">
        <ul>
          <li>Finish my BSc in Computer Science with a strong CGPA.</li>
          <li>Keep building hands-on SOC skills alongside my classes.</li>
          <li>Land a remote SOC analyst role before graduation.</li>
        </ul>
        <p class="muted">Track coursework on the <a href="planner.html">Academic planner</a> page.</p>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2>Certificates</h2>
    <div class="table-wrap">
      <table class="data-table">
        <caption class="muted">Courses and certifications I have completed</caption>
        <thead><tr><th scope="col">Certificate</th><th scope="col">Issuer</th><th scope="col">Date</th><th scope="col">Proof</th></tr></thead>
        <tbody>
          <tr><th scope="row">Networking Basics</th><td>Cisco Networking Academy</td><td>10 Nov 2026</td><td><a href="certificates/cisco-networking-basics.pdf">View PDF</a></td></tr>
          <tr><th scope="row">Cybersecurity</th><td>TS Academy</td><td>2026</td><td>On request</td></tr>
          <tr><th scope="row">Project Management</th><td>Google</td><td>2026</td><td>On request</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
""")

# ---------------- Manager ----------------
page("planner.html", "Academic Planner", "Interactive academic planner: add tasks, mark them done, delete them, and calculate CGPA.",
     head("Academic planner", "Plan your assignments and see your CGPA. Everything is saved in this browser only.") + """
<section class="section">
  <div class="container">
    <div class="stats">
      <div class="stat"><b id="stat-pending">0</b><span>Tasks pending</span></div>
      <div class="stat"><b id="stat-done">0</b><span>Tasks done</span></div>
      <div class="stat"><b id="stat-gpa">–</b><span>Current CGPA (5.0 scale)</span></div>
    </div>

    <div class="grid cols-2">
      <div class="panel gold">
        <h2>Tasks</h2>
        <form id="task-form" class="stack-form" novalidate>
          <label>Task <input name="title" type="text" placeholder="Submit CSC 101 assignment" required></label>
          <div class="row">
            <label>Course <input name="course" type="text" placeholder="CSC 101"></label>
            <label>Due date <input name="due" type="date"></label>
            <label>Priority
              <select name="priority"><option value="medium">Medium</option><option value="high">High</option><option value="low">Low</option></select>
            </label>
          </div>
          <p class="error" id="task-error" role="alert"></p>
          <button class="btn primary" type="submit">Add task</button>
        </form>
        <div class="filters" style="margin-top:1.4rem">
          <button class="chip on" type="button" data-task-filter="all">All</button>
          <button class="chip" type="button" data-task-filter="pending">Pending</button>
          <button class="chip" type="button" data-task-filter="done">Done</button>
        </div>
        <ul class="task-list" id="task-list" aria-live="polite"></ul>
      </div>

      <div class="panel leaf">
        <h2>CGPA calculator</h2>
        <table class="gpa-table">
          <thead><tr><th>Course</th><th>Units</th><th>Grade</th><th></th></tr></thead>
          <tbody id="gpa-body"></tbody>
        </table>
        <div class="actions">
          <button class="btn" type="button" id="add-course">Add course</button>
          <button class="btn" type="button" id="reset-courses">Clear all</button>
        </div>
        <p class="gpa-result" id="gpa-value" style="margin-top:1.4rem;margin-bottom:0">–</p>
        <p class="muted" id="gpa-units">0 credit units counted</p>
        <p><strong id="gpa-class"></strong></p>
        <p class="muted" style="font-size:.9rem">Grades: A = 5, B = 4, C = 3, D = 2, E = 1, F = 0.</p>
      </div>
    </div>
  </div>
</section>
""", extra='<script src="js/planner.js"></script>\n')

# ---------------- Contact ----------------
page("contact.html", "Contact", "Contact Clement Idongesit Sunday about SOC analyst opportunities and collaborations.",
     head("Contact", "Open to remote SOC analyst opportunities and project collaboration.") + """
<section class="section">
  <div class="container grid cols-2">
    <form id="contact-form" class="stack-form panel gold" novalidate>
      <h2>Send a message</h2>
      <label>Your name <input name="name" type="text" autocomplete="name" required></label>
      <span class="error" data-error-for="name" role="alert"></span>
      <label>Your email <input name="email" type="email" autocomplete="email" required></label>
      <span class="error" data-error-for="email" role="alert"></span>
      <label>Phone number <input name="phone" type="tel" inputmode="numeric" autocomplete="tel" placeholder="08012345678" required></label>
      <span class="error" data-error-for="phone" role="alert"></span>
      <label>Message <textarea name="message" required></textarea></label>
      <span class="error" data-error-for="message" role="alert"></span>
      <button class="btn primary" type="submit">Send message</button>
      <p id="form-status" role="status"></p>
    </form>
    <div>
      <h2>Other ways to reach me</h2>
      <dl class="facts">
        <dt>Email</dt><dd><a href="mailto:c.sunday4937@miva.edu.ng">c.sunday4937@miva.edu.ng</a></dd>
        <dt>GitHub</dt><dd><a href="https://github.com/kaytech-bit" rel="noopener">github.com/kaytech-bit</a></dd>
        <dt>Based in</dt><dd>Nigeria, working remotely</dd>
      </dl>
    </div>
  </div>
</section>
""")
print("Built", len(PAGES), "pages")
