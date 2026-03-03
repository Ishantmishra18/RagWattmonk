import { useEffect, useState } from "react";
import { askQuestion , fetchData } from "./api";


function App() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  useEffect(() => {
    const data =  fetchData();
    console.log("Fetched data:", data);
    setData(data);
  },[]);



  return (
   <div className="min-h-screen bg-gradient-to-br from-slate-900 via-black to-slate-800 text-white">
      {data.map((item) => (
        <div key={item.id} className="p-4 border-b border-gray-700">
          <h2 className="text-xl font-bold">{item.title}</h2></div>
          ))}
   </div>
  );
}

export default App;
