import React, {useState} from "react";
import axios from "axios";
import {Modal} from "react-bootstrap";

function LaureateCard({ laureate, updateSelectedLaureates }) {
    const [ checked, setChecked ] = useState(false);
    const [ showProfile, toggleShowProfile ] = useState(false);
    const [ answers, setAnswers ] = useState([]);

    const { Account: { accountId, firstname, lastname }, studies } = laureate;

    function updateChecked() {
        setChecked(!checked);
        updateSelectedLaureates(accountId, firstname, lastname);
    }

    function openProfile () {
        if (answers.length < 1) {
            // Get all questions and answers
            axios.get(process.env.REACT_APP_API_HOST +"/api/answers/account/"+ accountId +"/form/latest")
                .then((res) => {
                    setAnswers(res.data);
                    toggleShowProfile(true);
                })
                .catch(error => console.error("There was an error",error))
        } else {
            toggleShowProfile(true);
        }
    }

    return (
        <>
            <div className="card d-flex flex-row flex-nowrap align-items-center">
                <div className="card-body cursor-pointer py-3" onClick={openProfile}>
                    <h5 className='mb-1'>{firstname} {lastname}</h5>
                    {studies}
                </div>
                <div className="ml-auto mr-3">
                    <div className="custom-control custom-checkbox">
                        <input className='custom-control-input' type='checkbox' name={accountId} id={accountId} onChange={updateChecked}/>
                        <label className="custom-control-label" htmlFor={accountId} />
                    </div>
                </div>
            </div>

            <Modal show={showProfile} onHide={() => toggleShowProfile(false)}>
                <div className="modal-header">
                    <h5 className="modal-title">{firstname} {lastname}</h5>
                    <button type="button" className="close" onClick={() => toggleShowProfile(false)}>
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div className="modal-body">
                    {answers.map(({fkQuestionId, answer, Question : {question}}) => {
                        return (
                            <div className='py-2' key={fkQuestionId}>
                                <b>{question}</b><br/>
                                {answer}
                            </div>
                        )
                    })}
                </div>
            </Modal>
        </>
    );
}

export default LaureateCard
