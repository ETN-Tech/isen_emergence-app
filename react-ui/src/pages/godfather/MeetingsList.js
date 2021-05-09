import React, {useEffect, useState} from "react";
import {Button} from 'react-bootstrap';
import axios from "axios";
import Time from 'react-time';

function handleCall(godFatherId,laureateId,rategodfather)
{
        
        axios.put(process.env.REACT_APP_API_HOST +"/api/meetings/godfather/"+godFatherId+"/laureate/"+laureateId,{  
                                                                    godfatherRating:rategodfather
                                                                    
                                                                    
                                                                    })
        .then(res => {
            
            console.log(res)
        
             
         })
         .catch(error => console.error("There was an error",error))   
        

}




export default function MeetingsList({account}){
    const[meeting,setMeeting] = useState([])
    const [aaccount, setAccount] = useState([]);

    useEffect(() => {
        const options = {
            method: "GET",
            header:
            {
                'content-type': 'application/json',
                'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MTgxNDMxNzIsImV4cCI6MTYxODIyOTU3Mn0.5patB5mX43WUUsCHVPnoAbmz-rEnLwyqRLyAJCl_Ss0'
            }
        }
        fetch(process.env.REACT_APP_API_HOST +"/api/accounts",{options})
        .then(res => {
            res.json()
            .then(res => {
               
                return setAccount(res)
            })
            
        })
        
        .catch(error => console.error("There was an error",error)) 
       
    },[]);

    useEffect(() => {
        const options = {
            method: "GET",
            header:
            {
                'content-type': 'application/json',
                'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MTgxNDMxNzIsImV4cCI6MTYxODIyOTU3Mn0.5patB5mX43WUUsCHVPnoAbmz-rEnLwyqRLyAJCl_Ss0'
            }
        }
        fetch(process.env.REACT_APP_API_HOST +"/api/meetings",{options})
        .then(res => {
            res.json()
            .then(res => {
                
                return setMeeting(res)
            })
            
        })
        
        .catch(error => console.error("There was an error",error)) 
       
    },[]);


    return(
        
        <div className="container">
            
            <h1 className="p-5">Vos meeting : </h1>
            <div className="p-2 m-2 align-self-center">{meeting.map( meet=> meet.fkGodfatherAccountId===account.accountId?
                <div className="card p-5 d-flex flex-row m-2">
                    
                    <div className="col align-self-center"><div>{aaccount.map(acc=> acc.accountId===meet.fkLaureateAccountId?<div><h3>{acc.firstname} {acc.lastname}</h3><div><Time value={meet.beginning} format="HH:mm" />-<Time value={meet.ending} format="HH:mm" /></div></div>:false)}</div></div>
                    <div className="col align-self-center"><RadioButtons meeting={meet} accountid={account.accountId} name={meet.fkLaureateAccountId} laureateId={meet.fkLaureateAccountId}/></div>
                    
                </div>:false
                )}
                 </div>
        </div>
       )
}




function RadioButtons({ accountid, laureateId, name, meeting}){
    const[note, setNote] = useState(null);
    
    return(
        
        
        <div className="d-flex flex-row ">
            <div className="d-flex flex-row col">
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name={name} id="Radios1" value="1" onChange={(e) => setNote(e.target.value)}/></div>
                    <div><label htmlFor="Radios1">1</label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name={name} id="Radios2" value="2" onChange={(e) => setNote(e.target.value)}/></div>
                    <div><label htmlFor="Radios2">
                        2
                    </label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name={name} id="Radios3" value="3" onChange={(e) => setNote(e.target.value)}/></div>
                    <div><label htmlFor="Radios3">
                    
                        3</label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name={name} id="Radios4" value="4" onChange={(e) => setNote(e.target.value)}/></div>
                    <div><label htmlFor="Radios4">
                        4
                    </label></div>
                </div>
                
            </div>
            <div><div>{meeting.godfatherRating==null?<Button className=" align-self-center col "  variant="btn btn-success " onClick={()=>handleCall(accountid,laureateId,note)}>Envoyer</Button>:<div><Button className=" align-self-center col "  variant="btn btn-success " disabled>Envoyer</Button><div className="text-success align-self-center mt-3">envoyé</div></div>}</div></div>
        </div>
        


        
    )
}