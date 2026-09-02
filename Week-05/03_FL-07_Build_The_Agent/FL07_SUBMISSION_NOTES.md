# FL-07 Submission Notes

I built **StudyPilot — Personal BCA Study Coach** from my FL-06 specification.

The MVP is a working Python scripted agent with a live local-file connection to the `notes/` directory. Its core loop is: user request → search local notes → grounded response/plan/quiz → optional progress save.

I kept the scope narrow so the core job can run end to end without mid-run hand editing. I also added automated checks for note retrieval, missing information, planning, progress storage, and quiz generation.

The build log documents the iterations and the features deliberately cut from the FL-06 spec.

For the required run capture, I will record one continuous, raw session showing the request-to-result loop on my machine. I have not fabricated a screenshot or video.
