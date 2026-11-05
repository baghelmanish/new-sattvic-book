# Update reading-partners.html Section 1 to #FFFFFF for alternating rhythm
with open(r'd:\Sattvic Books\reading-partners.html', 'r', encoding='utf-8') as f:
    rp = f.read()

target_rp = '<section class="section-padding" id="contact-partnerships"\n            style="background-color: #FAF6EE;'
replacement_rp = '<section class="section-padding" id="contact-partnerships"\n            style="background-color: #FFFFFF;'

if target_rp in rp:
    rp = rp.replace(target_rp, replacement_rp)
    with open(r'd:\Sattvic Books\reading-partners.html', 'w', encoding='utf-8') as f:
        f.write(rp)
    print("Updated reading-partners.html Section 1 to #FFFFFF!")
else:
    print("Could not find Section 1 in reading-partners.html")

# Update press-release-diwali-launch.html line 163 to #FFFFFF
with open(r'd:\Sattvic Books\press-release-diwali-launch.html', 'r', encoding='utf-8') as f:
    pr = f.read()

target_pr = '<section class="section-padding" style="background-color: #FAF6EE;">'
replacement_pr = '<section class="section-padding" style="background-color: #FFFFFF;">'

if target_pr in pr:
    pr = pr.replace(target_pr, replacement_pr)
    with open(r'd:\Sattvic Books\press-release-diwali-launch.html', 'w', encoding='utf-8') as f:
        f.write(pr)
    print("Updated press-release-diwali-launch.html article body to #FFFFFF!")
else:
    print("Could not find section in press-release-diwali-launch.html")

