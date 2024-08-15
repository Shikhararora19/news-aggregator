import axios from 'axios'

function fetchNews(){
    axios.get('http://127.0.0.1:5000/api/news')
      .then((response) => {
        setData(response.data)
      })
      .catch((error) => {
        console.error('Error fetching data: ', error)
      })
}