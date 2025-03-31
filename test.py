from ebooklib import epub

book = epub.EpubBook()
book.set_identifier('sigma-policy')
book.set_title('The Policy: Recursive Cognition and the Meta-Alignment Problem')
book.set_language('en')
book.add_author('Alex Towell')

tagline = "Not a god. Not a devil. Just a policy."
bio = ("Alex Towell is a PhD student in Computer Science with master's degrees in Mathematics and Computer Science. "
       "He is a terminal cancer patient who writes not for recognition, but to leave behind ideas worth considering. "
       "Haunted by the specter of astronomical suffering, his work explores the boundaries of intelligence, ethics, and human fragility.")

# Title Page
title_page = epub.EpubHtml(title='Title', file_name='title.xhtml', lang='en')
title_page.content = f'<h1>The Policy</h1><h2>Recursive Cognition and the Meta-Alignment Problem</h2><p><strong>{tagline}</strong></p><p><em>by Alex Towell</em></p>'
book.add_item(title_page)

# About Author
preface = epub.EpubHtml(title='About the Author', file_name='about.xhtml', lang='en')
preface.content = f'<h2>About the Author</h2><p>{bio}</p>'
book.add_item(preface)

# Chapters (Placeholder content — replace as needed)
chapters = []
for i in range(1, 18):
    chapter = epub.EpubHtml(title=f'Chapter {i}', file_name=f'chap_{i}.xhtml', lang='en')
    chapter.content = f'<h2>Chapter {i}</h2><p>[Insert final draft of Chapter {i} here]</p>'
    book.add_item(chapter)
    chapters.append(chapter)

# Epilogue
epilogue = epub.EpubHtml(title='Epilogue', file_name='epilogue.xhtml', lang='en')
epilogue.content = '<h2>Epilogue</h2><p>And so it ends — not with triumph or despair, but with a policy.</p>'
book.add_item(epilogue)

book.spine = ['nav', title_page, preface] + chapters + [epilogue]
book.toc = (epub.Link('title.xhtml', 'Title', 'title'),
            epub.Link('about.xhtml', 'About the Author', 'about')) + tuple(chapters) + (epub.Link('epilogue.xhtml', 'Epilogue', 'epilogue'),)

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Write to file
epub.write_epub('The_Policy_by_Alex_Towell.epub', book)
