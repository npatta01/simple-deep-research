# Simple Deep Research Workshop

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/npatta01/simple-deep-research)

## About

This repository contains slides and notebooks for a hands-on workshop on implementing a Deep Research workflow with LangGraph.


## Deep Research

Deep Research is composed of the following steps:

![deep research flow](images/deep_research_flow.png)



## Notebooks

- [Setup](notebooks/00_setup.ipynb)

Validates that the API keys and Python environment are configured correctly.


- [LangGraph Basics](notebooks/01_langgraph_basics.ipynb)
- [LLM Basics](notebooks/01_llm_basics.ipynb)

Introduces the LangGraph and LLM concepts used throughout the workshop.

- [Scoping](notebooks/02_scoping.ipynb)


- [Research Step as an Agent](notebooks/03_research_as_agent.ipynb)

- [Write Report](notebooks/04_write_report.ipynb)

- [Full Graph](notebooks/05_full_graph.ipynb)



## Workshop Info

The notebooks require OpenAI and Tavily API keys.

During the workshop, a proxy server is used to avoid providing the keys.

To use your own keys or run the notebooks after the workshop, modify [env_workshop](env_workshop) and provide the keys under the `# using own keys` section.




## Sample Reports

Seattle coffee shops:

- [Gemini](https://gemini.google.com/share/0911c9b077e2) · [PDF](reports/report_gemini.pdf)
- [ChatGPT](https://chatgpt.com/share/690e8013-94cc-800a-9751-44d2a2c6f125) · [PDF](reports/report_chatgpt.pdf)
- [Repository report](reports/report_custom.md)



## Slides

[PyData 2025 workshop slides](artifacts/pydata_2025.pdf)




## Contact

For help or feedback, please reach out to:

- [Nidhin Pattaniyil](https://www.linkedin.com/in/nidhinpattaniyil/)   
- [Ravi Yadav](https://www.linkedin.com/in/ravi-kumar-yadav-535b268/)   



## Acknowledgment

The authors learned from LangChain Academy's [Deep Research with LangGraph](https://academy.langchain.com/courses/deep-research-with-langgraph) course.
