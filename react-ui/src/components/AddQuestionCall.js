import { useState } from "react";
import  React from "react"
import {useEffect} from "react"
import {Button, Modal} from 'react-bootstrap';
import { Field } from "./Field";
import axios from 'axios';

function handleAddQuestionCall()
{
        axios.post("https://etn-test.herokuapp.com/api/questions",{ question:question.value,description:description.value,fkFormId:"2"})  // à voir fillValue et formk?
        .then(res => {
            console.log(res)  
         })  
}




export function AddQuestionCall()
{

    const [show, setShow] = useState(false);
    const[exit,setExit] = useState(false)
    const [question, setQuestion] = useState("")
    const [description, setDescription] = useState("")
  
    const handleClose = () =>  setShow(false)  
  
    const handleShow = () => setShow(true);
    const handleExit = () => 
    {
        
        setExit(true)
    }

    return <div>
    <button onClick={handleShow}>Ajouter</button>
    {exit?
    <div className="container">

    <Field questionLabel={fillValue} />
    </div>:""}
   <Modal size="lg" show={show} onHide={handleClose}  > 
      <Modal.Header>  
          <Modal.Title>Ajouter une question </Modal.Title>
      </Modal.Header>
    <Modal.Body>
          <label htmlFor="question"> Question </label>
              <input  className="form-control mt-3" defaultValue="Name" required onChange={(event) => setQuestion(event.target.value)}type="text" id="question"/>

        <label htmlFor="description"> Description </label>
              <input  className="form-control mt-3" defaultValue="Description" required onChange={(event) => setDescription(event.target.value)}type="text" id="description"/>       
    </Modal.Body>
        
    <Modal.Footer>{/* Une fois qu'on a rentré les infos on les affiches avec un document.getElementbyId */}
      <Button variant="btn btn-success btn-sm" onClick={handleAddQuestionCall}> Enregister</Button>
          
      <Button variant="btn btn-danger btn-sm" onClick={handleClose}> <i class="me-2 bi-x-square-fill"></i> Fermer</Button>    

  </Modal.Footer>

  </Modal>

  </div>
}