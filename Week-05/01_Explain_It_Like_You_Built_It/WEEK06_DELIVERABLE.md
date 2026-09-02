# FlyRank AI Internship — Week 6
## Explain It Like You Built It

**Student:** Gungun Sharma  
**Track:** General AI Fluency  
**Week:** 6  
**Topic:** How my streaming AI chat works

### The real piece I chose

The part of my build I wanted to understand better was the **streaming AI chat flow** in my frontend AI project.

The main files involved are:

- `app/page.tsx` — the page that loads the chat experience.
- `components/chat.tsx` — the client-side chat interface where the user types and sees messages.
- `app/api/chat/route.ts` — the server-side route that receives the chat request and talks to the AI model.
- `lib/ai-config.ts` — the place where the AI configuration is kept separate from the UI.

### My explanation in simple words

I think of the chat as a small relay system.

First, I type a message in the chat box. The chat component sends my message to the application's chat API instead of calling the AI provider directly from the browser. This is important because the API key should stay on the server and should not be exposed in frontend code.

The request reaches `app/api/chat/route.ts`. This route is the middle layer between my website and the AI model. It receives the conversation messages, passes the relevant information to the model through the AI SDK, and asks for a **streaming** response.

The useful part of streaming is that the server does not have to wait for the complete answer before the user sees anything. The model can produce the response in small pieces, and those pieces are sent back while the answer is still being generated.

On the frontend, the chat component consumes that streamed response and updates the current assistant message as new text arrives. So instead of seeing:

> nothing → complete answer

the user experiences:

> nothing → first words → more words → more words → complete answer

That is why the interface feels like the AI is typing.

### Why I separated the UI and API

I originally thought of the chat as just a textbox connected to an AI model. After understanding the code, I realized there are actually two different jobs:

1. **Frontend:** collect the user's message and display the conversation.
2. **Server route:** securely communicate with the AI provider and return the generated response.

Keeping those responsibilities separate makes the project easier to understand and maintain. It also prevents the secret API key from being placed in client-side code.

### What Next.js is doing here

Next.js gives me the page structure and the API route in the same project. The browser can load the page, while the `/api/chat` route can run server-side.

So, in a simplified flow, my project works like this:

**User types message**
→ **Chat component**
→ **`/api/chat`**
→ **AI model**
→ **streamed response**
→ **Chat component**
→ **User sees the answer appear progressively**

The important thing I learned is that streaming is not a special visual animation. The UI is showing real pieces of the response as they become available.

### What I understand now

Before studying this part, the streaming chat looked like a complicated block of AI code to me. Now I understand the main responsibility of each layer.

I do not need to memorize every library function. I can explain the important idea: **the client sends the conversation to my server route, the server asks the AI for a streamed response, and the client renders that response as it arrives.**

That is the part of the build I can now explain to someone else without treating it as mystery code.

---

## Two quick examples

### Example 1 — Normal response

If the AI generates:

`Your project is using Next.js.`

a non-streaming implementation may wait for the complete sentence and then display it.

### Example 2 — Streaming response

With streaming, the user may see:

`Your`

then:

`Your project`

then:

`Your project is`

then:

`Your project is using`

and finally:

`Your project is using Next.js.`

The exact chunks are controlled by the streaming system, but the idea is that the UI receives the answer progressively.

---

## My final takeaway

The biggest thing I learned from this part is that an AI chat interface is not only an AI model. It is a flow between the browser, a server-side API route, and the model. Streaming makes that flow visible to the user by displaying the response while it is being generated.

**I chose this topic because it is a real piece of my own FlyRank frontend build, and understanding this flow makes me more confident that I can explain and maintain what I shipped.**
