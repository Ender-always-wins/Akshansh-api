<h1 class = "projects-header"> Akshansh-api </h1>

<p class = "projects-para">
    This is the backend, handling all the requests to github, and serving the data to the frontend, in order 
    to limit the number of requests to the github servers, via caching.
</p>

<p class = "projects-para">
    This has been written entirely in python using FastAPI and hosted at <a href = https://www.render.com id=hyperlink>render</a>.
</p>

<ul class = "projects-para" id = "endpoints-list">
    Right now I support three query parameters at the root endpoint
    <li>
        type: supports three values, "projects", "writeups" or "blogs"
    </li>
    <li>
        name: an optional parameter, if the name(string) is provided, only the details of that particular item will be returned
    </li>
    <li>
        names: another optional parameter, takes in a boolean value, if the said value is true then returns only a json object with the names of all items of the provided type, along with an index indicating the order in which they were published.
    </li>
</ul>