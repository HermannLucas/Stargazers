# Stargazers Neighbours

This application list all the star neighbours of a given Github repository.

This code has been tested and ran using python 3.8.12.

## Tests

to run the unittests do:
```bash
pip install -r requirements.txt
python -m unittest
```

## Run

To Start the server do the following:
```bash
pip install -r requirements.txt
GITHUB_ACCESS_TOKEN=<your-github-access-token> flask --app web run
```

This will will print some log while it starts the server.

```bash
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Serving Flask app 'web'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

Once you see the line `* Running on <http-url>` that means that the server is up and running at the given url.

you can now get the neighbours of a given repositories by querying the server by querying `<server-url>/repos/<user>/<repo>/starneighbours`.  
where:
  - `<user>` is the GitHub username of the owner of the repo you want to query
  - `<repo>` is the name of the repository you wish to query

### Example

To get the neighbours of the repo:
https://github.com/hermannlucas/adeventofcode

and given that the applications is accessible at `http://127.0.0.1:5000`

Using `curl` you would need to run:
```bash
curl http://127.0.0.1:5000/repos/hermannlucas/adeventofcode/starneighbours
```

It should give you the following JSON:
```json
[
   {
      "repo":"42Crunch/vscode-openapi",
      "stargazers":[
         "adampridmore",
         "HermannLucas"
      ]
   },
   {
      "repo":"softwaremill/tapir",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"nicolaka/netshoot",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"co-cddo/federated-api-model",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"EqualExperts/ee-tech-interviews-uk",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"toptal/gitignore.io",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"chunky/sqlraytracer",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"Redocly/redoc",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"scopt/scopt",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"swagger-api/swagger-core",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"heclak/community-a4e-c",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"Rexeh/joystick-diagrams",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"co-cddo/api-catalogue",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hmrc/accessibility-statement-frontend",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"electronicarts/CnC_Remastered_Collection",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"raml-org/webapi-parser",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hawgdar/hawgdar",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"rastapasta/mapscii",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"nihp-public/COVID-19-app-Android-BETA",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"Code52/carnac",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hmrc/accessibility",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hakluke/how-to-exit-vim",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"tldr-pages/tldr",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hmrc/off-payroll-decision",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"chbatey/scala-basics-talk",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee/eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"LeedsCodeDojo/Mastermind-June-2019",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"fpinscala/fpinscala",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hmrc/auth-client",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"hmrc/third-party-application",
      "stargazers":[
         "adampridmore"
      ]
   },
   {
      "repo":"HermannLucas/AdeventOfCode",
      "stargazers":[
         "HermannLucas"
      ]
   },
   {
      "repo":"adampridmore/advent-of-code-scala",
      "stargazers":[
         "HermannLucas"
      ]
   }
]
```
