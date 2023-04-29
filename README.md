# JCrew Slack Bot :shopping:

A chatbot hosted on the Slack UI that uses Langchain under the hood to help you answer any questions you may have about the wonderful products at JCrew.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

To demo the JCrew chatbot, you will need to create your own Slackbot first. You can find a tutorial [here]( https://slack.dev/bolt-python/tutorial/getting-started)! You will also need an OpenAI account to make API calls to the service. Make one [here](https://platform.openai.com/signup)! 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/icheng3/Instalily-CC-Chatbot.git
   ```
2. Install any dependencies.
    ```sh
   pip install -r requirements.txt
   ```
3. Copy .env.example to your own .env file and fill in the values for your OpenAI, Slack Bot, and Slack App tokens.


<!-- ROADMAP -->
## Roadmap

- [x] Scrape basic PDP data from JCrew
  - [ ] Scrape more thorough PDP data (sizes, colors, stock)
- [x] Integrate chatbot with Slack
- [x] Finetune chatbot with thorough specification of expectations delivered through the prompt.
  - [ ] Get it to say goodbye. Literally cannot work around this for some reason.


<!-- CONTACT -->
## Contact

Iris Cheng - iriscwen@gmail.com

Project Link: [https://github.com/icheng3/Instalily-CC-Chatbot/](https://github.com/icheng3/Instalily-CC-Chatbot/)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This was my first time working with Langchain (so cool) and I found these resources and repos to be the most helpful in guiding my project.
* [Learning about Langchain's conversational memory](https://www.pinecone.io/learn/langchain-conversational-memory/)
* [Redis guide on building an Ecommerce Chatbot](https://redis.com/blog/build-ecommerce-chatbot-with-redis/)
* [This repo by ibleducation deploying a mentor slack bot for its company](https://github.com/ibleducation/ibl-slack-chatgpt-langchain)
* [A quick start guide to understanding Langchain and how it works](https://www.youtube.com/watch?v=aywZrzNaKjs&t=338s&ab_channel=Rabbitmetrics)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
