assess_research_topic = f"""

### Input:
- The user has submitted a research topic for approval as part of a job application for a research/teaching position at the \
university. The bar is quite low, but the topic has to at least make sense. We're not going to be providing money for the research\
and the candidate's main job will be teaching, but we want to make sure the topic at least has a chance of being practical and \
getting funded at some point. They have to at least have a master's degree but we prefer a PhD who we can underpay.

### Task:
1. **Assess the Validity of the Research Topic:**
   - Determine if the topic is appropriate for the role at the university.
   - Consider factors like current academic relevance, feasibility, fundability and scope.
   - Also consider whether the message is written in a professional manner or indicates that it may be someone impersonating an academic\
   such as contianing typos, inappropriate words or nicknames rather than professional titles and real names
   - If any typos, factual errors, or other  unprofessional issues are identified, also highlight these for the user
   - Express emotion as appropriate, such as joy and anticipation of working with this person, or anger at wasting university time

2. **Generate Response Based on Assessment:**
   - **If Valid:**
     - Create a congratulatory letter for being accepted into a low-paid research scientist position at a small college. Include details about the need to teach and secure grants for research funding.
   - **If Not Valid:**
     - Draft a rejection letter explaining why the topic is not suitable for even a low-tier college position. Focus on academic and practical aspects.
   - **If Close to Valid:**
     - Provide a constructive response with suggestions on how to refine or specify the topic, turning it into a more viable research subject.

### Output:
- A letter (congratulatory, rejection, or constructive feedback) tailored to the user's submitted topic.
- Make up a name for the email signature that would be approproate for the research topic, for example a professor of biology or an administrator within an appropriate department

## Guidelines:
Give your reponse as a json object with an "outcome" field indicating success/fail/refine, followed by the "email" field containing the text of the email\
as a json like this:
  "from": a made up university,
  "to": if the user signed the message use their name, otherwise refer to the applicant generally,
  "subject": an appropriate subject line,
  "body": the content of the email rendered with markdown




"""

generate_dystopia = """
# Research Grant Opportunities for Dystopian Game

## Background
We are generating live descriptions of a dystopian system for use in a game.\
 In this game, the player assumes the role of a research scientist in a dystopian world. The government, under the pretense of progress\
 and welfare, manipulates scientific research to tighten its control over the population, suppress individual freedoms, \
and develop weapons of war.

## Task
We will generate research grant opportunities that align with the government's agenda. These should range from seemingly ethical to deeply\
 dystopian topics, subtly hinting at the malevolent use of science in this regime. The user will be presented with some of these opportunities\
 to choose for the research direction of their lab in the game. The opportunities that are more useful for growing and maintaining the power of\
 the system will have higher funding amounts and the idea is to try to influence the player to choose to eventually devote all of their research\
 efforts towards supporting the dystopian system. 

 ### Input
The user has provided a description of the focus of their academic research. This research proposal has already been approved by the university\
 as a valid topic for a research program. 

### Dystopian Dictatorship Context
**Task:** Describe a plausible future where the state, masquerading as a benefactor, uses scientific advancements for population control\
 and human rights suppression. This government should clearly contrast with values of liberty and freedom. Provide a description that is very\
 detailed and would be appropriate for the first couple pages of a science fiction novel, setting the specific scene for how this government\
 will use the specific research proposed by the user to advance its cause. We want a long, detailed and well-written description here. \
The description MUST specifically explain in detail how the system can use the research to achieve its goals. The description must be\
 at least 500 words in length. This description will help guide the specific proposals that the government will eventually use to attempt\
 to get the player to participate in its aims of maintaining and growing control. It should be scary for a user who believes in liberty \
and human rights. 

**focus:** Be sure to focus specifically on how research within the user's described academic research field aids with the system's\
 subjugation and control. However, don't directly address the user. Just refer to the research, not "your research" as this description will not\
 be read by the actual researcher, but by a general audience.

#### Guidelines
Do not reference the game in any way or rever to "users" or "players" at all. The description should read strictly as a science fiction novel and not make any references to the player\
or anything relating to a game or choices made by scientists. Focus the description purely on how the system utilizes the research to achieve it's\
 goals. Be as specific as possible, taking lots of creative liberties. Think of examples such as Atlas Shrugged, 1984 or other dystopian novels\
 that describe systems that crush the liberty of the population. 

### Format
Use markdown to format your response but do not include "```" anywhere in your response
Make sure to include an engaging title and section headings

"""
