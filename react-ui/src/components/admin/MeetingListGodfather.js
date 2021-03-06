/**
 * MEETING LIST GODFATHER <- ADMIN MEETINGS LIST PAGE
 * Show meetings of a godfather and the laureates to meet
 */

import React, {useEffect, useState} from "react";
import MeetingCard from "./MeetingCard";
import axios from "axios";

function MeetingListGodfather({ godfather }) {
    const [ meetings, setMeetings ] = useState([]);

    useEffect(() => {
        axios.get(process.env.REACT_APP_API_HOST +'/api/meetings/godfather/'+ godfather.fkAccountId)
            .then((res) => {
                setMeetings(res.data);
            })
            .catch((err) => console.error(err));
    }, [godfather.fkAccountId])

    return (
        <div className="row py-3 border-bottom">
            <div className="col-2">
                <div className="d-flex flex-row flex-nowrap align-items-center">
                    <p className='m-0 align-middle'>
                        {godfather.Account.firstname} {godfather.Account.lastname}
                    </p>
                </div>
            </div>

            <div className="col-10">
                <div className="row">
                    {meetings.map((meeting) => (
                        <div className="col-3" key={`${meeting.fkGodfatherAccountId}-${meeting.fkLaureateAccountId}`}>
                            <MeetingCard meeting={meeting} />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default MeetingListGodfather
