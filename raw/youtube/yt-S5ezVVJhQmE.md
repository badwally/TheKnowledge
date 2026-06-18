---
schema_version: 1
id: yt-S5ezVVJhQmE
type: youtube
title: 'AI & Text to SQL: How LLMs & Schema Power Data Analytics'
url: https://www.youtube.com/watch?v=S5ezVVJhQmE
authors:
- IBM Technology
ingested_at: '2026-06-17T20:57:37Z'
content_hash: sha256:2214d539c5939f5c3492a311e2cd8e35ab0d7b1461ebce6ccd10083fe18b329d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: IBM Technology
  channel_url: https://www.youtube.com/@IBMTechnology
  duration_seconds: 529
  caption_track: fetched
  snippet_count: 85
filter:
  score: 0.72
---
[0] Picture this scenario. You're a business analyst and your boss walks in the room and says, "Show me
[6] customers who spend over $500 since the start of the year, sorted by how much they spend. The data
[11] is sitting right there in your customers database with the names, the
[18] date and the total amount spent by these customers. You know exactly what you're
[25] looking for. Now, sure, you might have some dashboards that can get you close to this answer
[30] if they've already been made, or if there's an easy way to grab that data, maybe through an Excel
[34] file or some other option. But the moment that you need something different, maybe a different date
[39] range, or you want to combine this customer's data with another table, you need to use sequel.
[46] This is sequel, Structured Query Language, one of the most widely used programing languages in the
[52] world. If you work with data in any capacity, you're probably interacting with sequel whether you
[57] know it or not. But here's the thing. Even this relatively straightforward query requires knowing
[63] specific sequel syntax. So let's walk through what this actually says. Select
[70] name and total spent from the customer's table, which is name and total spent
[76] from customers where the date is greater than January 1st, 2025. So that's from this year.
[83] And the total amount spent is greater than 500. So that's only gonna grab rows with the total
[89] amount spent over $500. And finally, order by the total spent descending. So in descending order
[96] with the highest amount first. Every piece has to be exactly right. You can't say "show me name in
[102] total spent" or "since January 1st, 2025" instead of this specific format. This is the
[108] fundamental gap that most organizations face. The people who best understand the business questions
[113] are not necessarily the people who can write the complex database queries. And the people who can
[119] write the sequel aren't always available when you need that urgent analysis. For decades, this meant
[124] either learning sequel by yourself, waiting for a data analyst or settling for what your existing
[129] BI tools can provide. But large language models, the same AI technology we're seeing
[136] power generation tasks and other use cases, have completely changed this equation. LLM-based text
[143] to sequel is the process of taking a user's natural language question, running it through an
[150] LLM, generating a sequel query and then executing that
[157] query on a database, ultimately resulting in data coming back
[163] to the user. The concept seems straightforward, but this has been a challenge that
[170] prior to LLMs was extremely difficult to solve reliably. So here's how modern AI
[176] systems actually make this work. To understand the process. Let me walk through an example that
[182] illustrates the key steps. And we'll use movies because who doesn't love movies? So imagine you
[188] have a movie database like IMDb and someone asks "what movies were directed by Christopher Nolan?" So
[194] let's break down how text to sequel can help with this question. We'll do this in two parts.
[201] So part one is schema understanding.
[211] The AI needs to understand what our database looks like. We can solve this problem by providing
[216] the LLM the database schema, which is the structure of your tables and columns, things like
[223] director name, rating or maybe the box office
[230] and how it did on the opening weekend. The AI needs to understand this because it needs to
[236] learn your technical structure of the database that it's using, However, modern systems need to go
[241] further than just understanding the director name or ratings or box office. They also need to
[246] understand your business context.
[254] In your movie database, if someone asks for recent movies, the LLM needs to know that recent movies in
[260] your database means released in the last two years, or that top rated or ratings refers to
[266] movies with an IMDb rating above an eight. Also, systems learn from successful
[273] past queries. So, for example, if I've previously asked what sci-fi movies do I have
[280] in my database and the system generates the right sequel, it can remember that pattern for future
[286] genre-based questions. So our LLM combines our schema understanding and structural knowledge of
[293] our personal movie collection, as well as how it's broken down based on business context and past
[298] queries to help it understand how you think and organize your movies. Part two is
[305] content linking. Real-world databases are messy.
[312] That director's name might be stored as Chris Nolan,
[319] could be stored as C dot Nolan or it could be stored as Nolan
[326] comma Chris. There's a million different ways you can enter someone's name.
[332] And so the AI needs to handle this through what we call semantic matching.
[343] The system doesn't just look for exact matches to Christopher Nolan. It understands that all three
[349] of these variations refer to the same person, and can generate the sequel that helps find them all.
[354] This works because the AI can analyze your actual database content and create what's called vector
[362] representation.
[369] This is essentially a mat mathematical fingerprint of each piece of data, and so similar names like
[374] Chris Nolan, C Nolan, Nolan, Chris, as well as Christopher Nolan, how we all know him, ah can get the
[380] similar fingerprint so the AI can recognize those variations automatically. The same principle
[386] applies to your business data, product names, customer categories, department names. Any field
[392] where the entry isn't perfect or standardized over time can value from content linking. So,
[399] between schema understanding and content linking,
[406] modern AI systems can handle both the structure and the messiness of real databases
[413] representing major breakthroughs that makes text to sequel practical. Now, this technology is
[419] impressive, but we need to be realistic about where we are. There are performance benchmarks. One
[425] of the most popular is called bird, that test LLM-based sequel systems against messy,
[431] real-world databases instead of cleaned up academic datasets typically used in research. The
[437] results reveal where current systems still struggle. So first is with scale
[443] and performance. Academic datasets are small and controlled,
[450] but production databases can have thousands of tables and millions of rows. Generating efficient
[456] SQL that runs quickly on these massive datasets requires optimization skills that current AI
[461] systems are still developing. The second is edge cases and
[468] unusual data patterns. Real-world databases contain unexpected relationships, legacy data
[474] structures and unique business scenarios that, when systems encounter these edge cases, they can
[480] produce sequel that doesn't have the correct syntax or returns incorrect values. However, the systems
[485] that work best today are rapidly improving, and they're combining robust schema
[492] understanding, as well as content linking, with better optimization
[498] techniques and domain-specific training. LLM-based text to sequel represents a fundamental shift
[505] from requiring sequel expertise to enabling natural language data exploration. The technology isn't
[512] perfect yet, but is very practical for common questions, and it's already changing how
[516] organizations access data. So next time your boss walks in asking for those customer insights, or
[522] you want to find out all about Christopher Nolan movies. The barrier between you and answering that
[527] question is finally starting to disappear.
