# Week 6 Tutor Check — Streaming AI Chat

## What I had to learn

I used the streaming AI chat flow from my own frontend project as the topic for Week 6.

### Question 1
**Why should the AI provider API key be kept in the server-side route instead of directly in the browser code?**

**My answer:**  
Because frontend code runs in the user's browser, so a secret placed there can potentially be exposed. The server-side route is the safer place to read the secret environment variable and make the provider request.

**Correction/check:**  
Correct. The important idea is that secrets belong on the server, not in client-side code.

### Question 2
**What is the main difference between a normal AI response and a streamed response?**

**My answer:**  
A normal response can wait for the whole generated answer before showing it. A streamed response sends the generated output progressively, so the UI can show the answer while it is still being produced.

**Correction/check:**  
Correct. Streaming changes when the data becomes available to the UI; it is not simply a fake typing animation.

## What I can explain now

I can describe the flow as:

**Browser/chat UI → Next.js API route → AI model → streamed response → browser/chat UI**

I understand the purpose of each part instead of only knowing that the code makes the chatbot work.
