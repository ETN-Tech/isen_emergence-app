/**
 * ADMIN HOME PAGE
 * Show a dashboard for the admin with actions
 */

import React, {useEffect, useState} from "react";
import {Container} from 'react-bootstrap';

import AccountInfos from "../../components/commons/AccountInfos";

export function Home({ phase, updatePhase, account }) {
    const [ btn, setBtn ] = useState();

    useEffect(() => {
        // Check if godfather should interact at this phase
        if ([1, 2, 3, 4, 5, 6, 7].includes(phase.phaseId)) {
            setBtn(<a className="btn btn-primary btn-lg" href={`${phase.buttonLink}`} role="button">{phase.buttonText.replace('[]', 'parrain/filleul')}</a>);
        } else {
            setBtn();
        }
    }, [phase])

    return (
        <Container className='py-4'>
            <div className="jumbotron">
                <h1 className="display-4">Bienvenue {account.firstname} !</h1>
                {phase.phaseId !== undefined ? (
                    <>
                        <p className="lead"><span className='badge badge-primary'>Phase {phase.phaseId}</span> { phase.lead.replace('[]', 'parrain/filleul') }</p>
                        <hr className="my-4"/>
                        <div className='d-flex justify-content-between'>
                            { btn }
                            <button className='btn btn-secondary' onClick={() => updatePhase(phase.phaseId + 1)}>Phase suivante &rsaquo;</button>
                        </div>
                    </>
                ) : null}
            </div>

            <div className="py-4">
                <h2>Tableau de bord</h2>

                <AccountInfos account={account} />
            </div>
        </Container>
    )
}
