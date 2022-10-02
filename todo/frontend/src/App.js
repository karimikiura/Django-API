import React, {Component} from 'react'
import axios from 'axios'

const list = [
      {
        "id": 1,
        "title": "HTTP Verbs",
        "body": "Hyper Text Transfer Protocol is the backbone of the request/response cycle over the internet. Introduced by Tom Brenners in UK Labs.\r\nThe verbs describe actions such as;\r\n1. PUT\r\n2. CREATE\r\n3. DELETE\r\n4. READ",
        "slug": "http-verbs"
    },
    {
        "id": 2,
        "title": "Django slug",
        "body": "Sjango slug is a newspaper term. Replaces the use of id to improve search engine ranking.",
        "slug": "django-slug"
    },
    {
        "id": 3,
        "title": "PrePopulated Fields",
        "body": "Manually adding a slug field each time quickly becomes tedious. So we can use a prepopulated_field in the admin to automate the process for us.",
        "slug": "prepopulated-fields"
    }
]


class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list };
  }

  render() {
    return(
      <div>
        { this.state.list.map(item => (

          <div key = { item.id }>
            <h1>{ item.title }</h1>
            <p>{ item.body } </p>

          </div>
        ))}
      </div>
    );
  }
  }

export default App