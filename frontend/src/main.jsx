import React from 'react'
import { createRoot } from 'react-dom/client'
import axios from 'axios'

function App(){
  const [plans, setPlans] = React.useState([])
  const [debates, setDebates] = React.useState([])

  React.useEffect(()=>{
    axios.get('http://localhost:3000/api/plans').then(res=>setPlans(res.data))
    axios.get('http://localhost:3000/api/debates').then(res=>setDebates(res.data))
  },[])

  return (
    <div style={{fontFamily: 'Arial, sans-serif', padding: 20}}>
      <h1>Rugby Session Plan Debate System</h1>
      <section>
        <h2>Session Plans</h2>
        <ul>
          {plans.map(p => (
            <li key={p.id}><strong>{p.title}</strong> — {p.author} — {p.points}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Debates</h2>
        <ul>
          {debates.map(d => (
            <li key={d.id}>Plan {d.planId}: {d.author} — {d.comment}</li>
          ))}
        </ul>
      </section>
    </div>
  )
}

createRoot(document.getElementById('root')).render(<App />)
