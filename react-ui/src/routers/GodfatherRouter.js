/**
 * GODFATHER REACT ROUTER
 * Include Godfather Navigation
 * Route to targeted page's component
 */

import React from "react";
import {BrowserRouter, Route, Switch} from 'react-router-dom';

// Import pages
import {Preselections} from "../pages/godfather/Preselections";
import {Home} from "../pages/godfather/Home";
import MeetingsList from "../pages/godfather/MeetingsList";
import Matches from "../pages/godfather/Matches";
import NotFound from "../pages/NotFound";

import {GodfatherNav} from "../navigation/GodfatherNav";

export default function AdminRouter({ phase, account }) {

    return (
        <BrowserRouter>
            <GodfatherNav phase={phase} />

            <Switch>
                <Route exact path='/'>
                    <Home phase={phase} account={account} />
                </Route>
                {phase.phaseId === 3 ? (
                    <Route path='/preselections'>
                        <Preselections account={account} />
                    </Route>
                ) : null}
                {phase.phaseId === 5 ? (
                    <Route path='/meetings'>
                        <MeetingsList account={account} />
                    </Route>
                ) : null}
                {phase.phaseId === 7 ? (
                    <Route path='/matches'>
                        <Matches account={account} />
                    </Route>
                ) : null}

                {phase.phaseId !== undefined ? (
                    <Route path='/*'>
                        <NotFound/>
                    </Route>
                ): null}
            </Switch>
        </BrowserRouter>
    )
}
