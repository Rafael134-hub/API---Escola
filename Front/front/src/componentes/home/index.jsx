import React, {useState, useEffect} from "react";
import './styles.css'
import axios from "axios";

export default function Home(){
  const token = localStorage.getItem('token')
  console.log('Token Home: ', token)
  useEffect(() => {
      const fetchData = async () =>{
        try {
            const response = await axios.get(
              'http://127.0.0.1:8000/teachers1/',
              {
                headers: {
                  Authorization: `Bearer ${token}`
                }
              }
              

            )
        } catch (error) {
          
        }
      }  
  }, [])

  return(
    <>
      <h1>Jiafei</h1>
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwoATkO8TZF-stgJ5Cb8Rm3BEN2xPfaIdXZQ&s"/>
      


    </>
  )
}

