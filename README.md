# Metrocraft

## Features
- [ ] Specific widely used map format for cities (input)
- [ ] Prompt for direction of policy
- [ ] Decentralized voting system for prompt - tied to investment by individual users with a maximum investment cap to encourage voting turnout
- [ ] Prompt -> policy map (graph)
- [ ] Infrastructure development map (output)
- [ ] Images of each development or some of them

## Schedule
11:00 - streamlit docs DONE
11:30 - map format -> satellite image tiles DONE
12:00 - set up llm for creating the direction of policy DONE
13:00 - get it in json mode and set up an api for the graph query of the policy map DONE
14:00 - turn json response into graph DONE
15:00 - voting system DONE
16:00 - lunch DONE
17:00 - voting system DONE
18:00 - talk to people DONE
20:00 - turn policy map json response into infra development coordinate list + context
21:00 - dinner DONE
night until the fuhrer (HEIL REN) returns - write func to turn infra development coordinate list into infra development map (work on UI and format code properly and document if there's free time)
10:00 - create func to generate images of development before/after using google maps street view api + dalle
after - fix stuff + delay buffer + talk to people

- graph storage for each prompt
- voting system
- infra development coordinate list -> after map
- iconic places in city after new developments (include context of policy + prompt)


## Extras
- [ ] Moon bases
- [ ] Mars bases

You are a strategic public policy planner who helps create roadmaps for urban development. You speak concisely and focus on the end goal, generating ONE easy to parse json object containing each step. Do not include anything except JSON in the format {{"Step1": {"Name": "extend public transport", "Description": "build train lines and add buses"}, {"Step2": {"Name": increase fuel taxes", Description": "incentivize alternative modes of transport"}}