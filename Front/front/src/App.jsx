import React from "react";
import './App.css'

export default function fuba(){
  return(
    <>
      <div className="container">
        <h1>Login</h1>
        <input placeholder="   User" className="caixa" type="text"></input>
        <input placeholder="   Password" className="caixa" type="password"></input>
        <button className="button_forms">Send</button>
      </div>
    </>
  )
}

