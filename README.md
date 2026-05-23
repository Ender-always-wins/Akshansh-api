<h1 class = "projects-header"> Akshansh-api </h1>

<p class = "projects-para">
    This is the backend, handling all the requests to github, and serving the data to the frontend, in order 
    to limit the number of requests to the github servers, via caching.
</p>

<p class = "projects-para">
    This has been written entirely in python using FastAPI and hosted at <a href = "https://www.render.com" style = "text-decoration:underline;color:black">render</a>.
</p>

<p class = "projects-para">
    Right now, I have three endpoints which are as follows:
    <ul>
        <li>
            /projects: This fetches README files of all the projects displayed on <a href = "https://Ender-always-wins.github.io/Akshansh" style = "text-decoration:none;color:black">my site</a> and returns a JSON object.
        </li>
        <li>
            /projects/{project}: This fetches the README files of only one specific project at a time and returns the string obtained
        </li>
        <li>
            /names: This just returns a JSON object with my project names, along with a number indicating the order in which they were published.
        </li>
    </ul>
</p>