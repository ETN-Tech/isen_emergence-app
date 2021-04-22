import React, {useEffect, useState} from "react";
import {Button} from 'react-bootstrap';
import axios from "axios";
import Time from 'react-time';

function handleCall(godFatherId,laureateId,rategodfather)
{
        
        axios.put("https://etn-test.herokuapp.com/api/meetings/godfather/"+godFatherId+"/laureate/"+laureateId,{  
                                                                    godfatherRating:rategodfather
                                                                    
                                                                    
                                                                    })
        .then(res => {
            console.log(res)
            
             
         })
         .catch(error => console.error("There was an error",error))   
         return issend

        }


export default function MeetingList({account}){
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
        fetch("https://etn-test.herokuapp.com/api/accounts",{options})
        .then(res => {
            res.json()
            .then(res => {
                console.log(res)
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
        fetch("https://etn-test.herokuapp.com/api/meetings",{options})
        .then(res => {
            res.json()
            .then(res => {
                console.log(res)
                return setMeeting(res)
            })
            
        })
        
        .catch(error => console.error("There was an error",error)) 
       
    },[]);


    return(
        
        <div className="container">
            
            <h1 className="p-5">Vos meeting : </h1>
            <div className="p-2 m-2 align-self-center">{meeting.map( meet=> meet.fkGodfatherAccountId==account.accountId?
                <div className="card p-5 d-flex flex-row m-2">
                    
                    <div className="col align-self-center"><div >{aaccount.map(acc=> acc.accountId==meet.fkLaureateAccountId?<div><h3>{acc.firstname} {acc.lastname}</h3><div><Time value={meet.beginning} format="HH:mm" />-<Time value={meet.ending} format="HH:mm" /></div></div>:false)}</div></div>
                    <div className="col align-self-center"><RadioButtons accountid={account.accountId}  laureateId={meet.fkLaureateAccountId}/></div>
                    
                </div>:false
                )}
                 </div>
        </div>
       )
}




function RadioButtons({accountid,laureateId}){

    const[note, setNote] = useState(null);
    const[issend, setSend] = useState(false);
    return(
        
        
        <div className="d-flex flex-row ">
            <div className="d-flex flex-row col">
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name="exampleRadios" id="exampleRadios1" value="1" onChange={(e) => setNote(e.target.value)}></input></div>
                    <div><label htmlFor="exampleRadios1">1</label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name="exampleRadios" id="exampleRadios2" value="2" onChange={(e) => setNote(e.target.value)}></input></div>
                    <div><label htmlFor="exampleRadios2">
                        2
                    </label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name="exampleRadios" id="exampleRadios3" value="3" onChange={(e) => setNote(e.target.value)}></input></div>
                    <div><label htmlFor="exampleRadios3">
                    
                        3</label></div>
                </div>
                <div className="form-check align-self-center d-flex flex-column">
                    <div><input type="radio" name="exampleRadios" id="exampleRadios4" value="4" onChange={(e) => setNote(e.target.value)}></input></div>
                    <div><label htmlFor="exampleRadios4">
                        4
                    </label></div>
                </div>
            </div>
            <div><Button className=" align-self-center col "  variant="btn btn-success " onClick={()=>handleCall(accountid,laureateId,note),()=>setSend(true)}>Envoyer</Button><div>{issend==true?<div className="text-success align-self-center">envoyé</div>:false}</div></div>
            

        </div>


        
    )
}