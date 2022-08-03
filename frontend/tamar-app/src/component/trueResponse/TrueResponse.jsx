import './TrueResponse.css'
import React from 'react'

export default function TrueResponse(props) {
    const btncontinue=()=>{
        // Continue to pay...
    }

    return (
        <div>
            <div className='txt'>Request approved - continue loading and paying</div>
            <button onClick={btncontinue} className="btn">continue</button>
        </div>
    )
}