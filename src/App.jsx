import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [data, setData] = useState(null)
  
  useEffect(() => {
    const source = axios.CancelToken.source();
    axios.get('http://127.0.0.1:5000/api/news', {cancelToken: source.token})
      .then((response) => {
        setData(response.data)
        source.cancel;
      })
      .catch((error) => {
        console.error('Error fetching data: ', error)
      })

  

  },[])



  return (
    <>
    <h1>Top 10 news today</h1>
    <ul className="news">
      {data ? data.map((news, index) => (
       
        <li key={index} className="news-item">
          <h2>{news.title}</h2>
          <img src={news.urlToImage} width={500} ></img>
          <h3>Author: {news.author}</h3>
          <p>{news.description}</p>
          <a href={news.url} target="_blank" rel="noreferrer">Read more</a>
        </li>
        
      )) : 'Loading...'}
      </ul>


    </>
  )
}

export default App
