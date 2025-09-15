# our recent purchase?"

/

42

/

In the above example, the initial user message is sent to triage_agent. Recognizing thatŒ the input concerns a recent purchase, the triage_agent would invoke a handop to the order_management_agent, transferring control to itu

This pattern is especially epective for scenarios like conversation triage, or whenever you prefer specialized agents to fully take over certain tasks without the original agent needing to remain involved. Optionally, you can equip the second agent with a handop back to the original agent, allowing it to transfer control again if necessary.

23

A practical guide to building agents