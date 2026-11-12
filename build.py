#!/usr/bin/env python3
"""Generates index.html for the portfolio. Edit the data below, then run: python3 build.py"""
from html import escape as e

GH = "https://github.com/Githaiga701"

FEATURED = [
    dict(
        title="Whizperz Tours & Safaris",
        kind="Booking platform", cats="web payments",
        lead="A tour company needed to take bookings and money online without hiring a developer for every change.",
        did=[
            "Five ways to pay in one checkout: M-Pesa, Pesapal, iPOS, Unipesa and crypto, with quotes, refunds and emailed receipts.",
            "An admin where staff add journeys, set prices, upload photos and manage user logins.",
            "Unit, API and browser tests, and a packaging script for cPanel hosting.",
        ],
        stack="TypeScript, M-Pesa Daraja, Pesapal IPN, automated tests, cPanel",
        links=[("View the code", f"{GH}/whizperzz")],
    ),
    dict(
        title="Buffalo Plains Adventures",
        kind="Live safari booking site", cats="web",
        lead="I run this site end to end: development, hosting, admin tools, content and compliance.",
        did=[
            "Traced an 8.7 second Largest Contentful Paint to its causes and fixed it with code splitting, lazy loading, WebP images and cache headers.",
            "Built a serverless back office on Vercel functions and Google Sheets that produces PDF invoices.",
            "Wrote the privacy policy and terms to comply with the Kenya Data Protection Act.",
        ],
        stack="React, TypeScript, Vite, Tailwind CSS, Vercel, jsPDF",
        links=[("Visit the site", "https://buffaloplainsadventures.com"), ("View the code", f"{GH}/Buffalo-Plains-Adventures")],
    ),
    dict(
        title="Damani FuelTech",
        kind="Forecourt automation", cats="infrastructure",
        lead="A fuel station platform built around the Technotrade PTS-2 controller, with a companion app on Google Play.",
        did=[
            "Wrote the integration reference: dispensers, tank gauges, leak sensors, payments, RFID, CCTV, GPS and KRA eTIMS.",
            "Built a Playwright crawler that maps every screen of the multi-branch web app.",
            "Turned that map into training and troubleshooting guides for station staff.",
        ],
        stack="Technotrade PTS-2, Playwright, technical writing",
        links=[],
    ),
]

PROJECTS = [
    ("LogisticsWeb", "web", "Fleet and delivery platform",
     "Drivers, vehicles, clients and jobs in one system, with assignment conflict checks, a full audit trail and a one-tap mobile view for drivers.",
     "React, Fastify, PostgreSQL, Prisma, Redis", [("Code", f"{GH}/LogisticsWeb")]),
    ("Vehicle Rental Platform", "web", "Rental marketplace for Kenya",
     "Owners list vehicles and renters book them. Phone OTP login, KYC document review, owner approvals, ratings and driver payment confirmation links.",
     "Next.js, NestJS, PostgreSQL, Turborepo", [("Code", f"{GH}/vehiclerentalservice")]),
    ("M-Pesa water tap", "payments infrastructure", "Hardware payment bridge, in development",
     "An ESP32 and relay bridge that lets a coin-operated community tap release 20 litres once M-Pesa confirms payment.",
     "ESP32, M-Pesa Daraja", []),
    ("M-Pesa STK Push integration", "payments", "Server-side payments",
     "A Daraja M-Pesa Express flow with a callback endpoint, sandbox and live modes, and credentials kept on the server.",
     "Next.js, TypeScript, Daraja API", [("Code", f"{GH}/Portifolio")]),
    ("OmniLife OS", "web", "Personal operating system",
     "A dashboard for projects and finances, with a database fallback that keeps the app building and rendering without a connection string.",
     "Next.js, Prisma, PostgreSQL", [("Live", "https://omnilife-os.vercel.app"), ("Code", f"{GH}/omnilife-os")]),
    ("Urban Digital Technologies", "web", "Company website",
     "Designed and built the site for an IT services provider, with a serverless contact form, email delivery and reCAPTCHA v3 spam protection.",
     "Next.js, Tailwind CSS, SendGrid", [("Live", "https://urban-dig-tech.vercel.app"), ("Code", f"{GH}/UrbanDigTech")]),
    ("Gym Management System", "web", "Membership system",
     "Members, subscriptions and records for gym owners and managers.",
     "PHP, MySQL", [("Code", f"{GH}/gym_management")]),
    ("Smart Applications International", "web security", "Website audit",
     "Audited the company's online shop and delivered a written report with findings ranked by priority.",
     "Audit, reporting", []),
    ("Cerber ransomware threat hunt", "security", "Incident investigation",
     "Followed a ransomware attack through the Splunk BOTSv1 dataset, from the first infected machine to the encrypted file server, and wrote the incident timeline.",
     "Splunk, SPL", []),
    ("Log4Shell analysis", "security", "Vulnerability study",
     "Scored the Log4Shell vulnerability with CVSS and proposed a SIEM set-up to detect attempts to exploit it.",
     "CVSS, SIEM design", []),
    ("PyScanner", "security", "Scanning utility",
     "A Python tool for vulnerability enumeration and scanning, built for automation and readable results.",
     "Python", []),
    ("Windows Server 2022 migration", "infrastructure", "Server estate migration",
     "Moved a simulated organisation to Windows Server 2022: Active Directory, DNS, DHCP, IIS, WSUS and a MailEnable mail server, with nine documentation deliverables.",
     "Windows Server, Active Directory, IIS", []),
    ("Multi-site network", "infrastructure", "Network lab",
     "Two sites joined by site-to-site VPN, with pfSense firewalls, HAProxy SSL offloading, Hyper-V and Active Directory.",
     "pfSense, HAProxy, Hyper-V", []),
    ("Storage and delivery labs", "infrastructure", "Performance testing",
     "TrueNAS and iSCSI throughput tests at 1 and 10 Gbps, a multi-node Hadoop cluster on EC2, and CDN origin tests at up to 100,000 concurrent streams.",
     "TrueNAS, iSCSI, AWS EC2", []),
]

EXPERIENCE = [
    ("2024 to now", "Infrastructure and Security Engineer", "Freelance, Kenya",
     "I build and run web platforms for Kenyan businesses: booking systems, payment integrations, performance work, documentation and security reviews. Clients include Buffalo Plains Adventures, Whizperz Tours & Safaris, Damani FuelTech, Urban Digital Technologies and Smart Applications International."),
    ("2022 to 2024", "IT Support and Systems Consultant", "Freelance, Ongata Rongai",
     "Day-to-day support for small businesses and individuals, including Zaaabel and Atlantis Dubai: computers, printers, networks, email and Microsoft 365. Set up LANs, Wi-Fi, firewalls and backups, and wrote handover notes so clients could handle routine fixes."),
    ("May to August 2023", "ICT Industrial Attachment", "County Government of Nyeri, Department of Transport, Public Works, Infrastructure and Energy",
     "Repaired and maintained ICT equipment, assembled system units, installed operating systems and software, ran backups and updates, and networked office systems."),
    ("2022", "Tech Consultant", "Riset Software & Systems, Kitengela",
     "Advised clients on software and systems, supported deployments and handled first-line technical questions."),
]

SKILLS = [
    ("Web and software", ["TypeScript and JavaScript", "React, Next.js, Vite", "NestJS, Fastify, Node.js", "PHP, Python, SQL", "PostgreSQL, MySQL, Prisma, Redis", "Tailwind CSS, shadcn/ui"]),
    ("Payments", ["M-Pesa Daraja, STK Push and callbacks", "Pesapal and IPN registration", "iPOS, Unipesa, crypto checkout", "Refunds, quotes and receipts", "PDF invoices"]),
    ("Systems and networks", ["Linux administration, Bash", "Windows Server 2019 and 2022", "Active Directory, DNS, DHCP, IIS, WSUS", "pfSense, HAProxy, VPN, VLANs", "Proxmox, VMware, Hyper-V", "TrueNAS, iSCSI, AWS EC2"]),
    ("Security", ["Splunk threat hunting", "Vulnerability scanning", "CVSS scoring and SIEM design", "System hardening and access control", "Kenya Data Protection Act compliance"]),
    ("Delivery", ["Vercel, Docker, cPanel", "Git and GitHub", "Turborepo and pnpm monorepos", "Unit, API and browser tests", "Playwright", "Core Web Vitals tuning"]),
    ("Support and writing", ["Hardware and software troubleshooting", "Microsoft 365", "User training", "Technical documentation and user guides", "Website and social media content"]),
]

def links_html(links, cls="text-link"):
    return "".join(f'<a class="{cls}" href="{e(u)}" target="_blank" rel="noopener">{e(t)}<span class="sr-only"> (opens in a new tab)</span></a>' for t, u in links)

def featured_html():
    out = []
    for p in FEATURED:
        did = "".join(f"<li>{e(d)}</li>" for d in p["did"])
        links = f'<div class="card-links">{links_html(p["links"])}</div>' if p["links"] else ""
        out.append(f'''
      <article class="glass feature" data-cats="{p["cats"]}">
        <div class="feature-head">
          <p class="kind">{e(p["kind"])}</p>
          <h3>{e(p["title"])}</h3>
          <p class="feature-lead">{e(p["lead"])}</p>
        </div>
        <div class="feature-body">
          <ul class="did">{did}</ul>
          <p class="stack"><span class="sr-only">Built with: </span>{e(p["stack"])}</p>
          {links}
        </div>
      </article>''')
    return "".join(out)

def projects_html():
    out = []
    for title, cats, kind, text, stack, links in PROJECTS:
        l = f'<div class="card-links">{links_html(links)}</div>' if links else ""
        out.append(f'''
      <article class="glass card" data-cats="{cats}">
        <p class="kind">{e(kind)}</p>
        <h3>{e(title)}</h3>
        <p>{e(text)}</p>
        <p class="stack"><span class="sr-only">Built with: </span>{e(stack)}</p>
        {l}
      </article>''')
    return "".join(out)

def experience_html():
    return "".join(f'''
      <li class="role">
        <p class="when">{e(when)}</p>
        <div class="glass role-card">
          <h3>{e(title)}</h3>
          <p class="org">{e(org)}</p>
          <p>{e(text)}</p>
        </div>
      </li>''' for when, title, org, text in EXPERIENCE)

def skills_html():
    return "".join(f'''
      <div class="glass skill">
        <h3>{e(name)}</h3>
        <ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul>
      </div>''' for name, items in SKILLS)

TEMPLATE = open("template.html", encoding="utf-8").read()
html = (TEMPLATE
        .replace("{{FEATURED}}", featured_html())
        .replace("{{PROJECTS}}", projects_html())
        .replace("{{EXPERIENCE}}", experience_html())
        .replace("{{SKILLS}}", skills_html()))
head, body = html.split("<body>", 1)
import re
body = re.sub(r"(?<![\w/.@-])(M-Pesa|PTS-2)(?![\w-])", r'<span class="nb">\1</span>', body)
html = head + "<body>" + body
assert "{{" not in html
open("index.html", "w", encoding="utf-8").write(html)
print("index.html written:", len(html), "bytes")
