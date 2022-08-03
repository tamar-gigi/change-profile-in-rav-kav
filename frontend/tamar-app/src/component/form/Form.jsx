import React from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { useNavigate } from 'react-router-dom';
import './Form.css'
import {  useState } from 'react';
import MyModal from "../modals/MyModal";


export default function Form(){
    // Variable settings
    const navigate=useNavigate();
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [idNumber, setidNumber] = useState('');
    const [noFile, sentNofile] = useState(false)
    const [valid, setValid]=useState(false);
    const [validF, setValidF] = useState(false);
    const [validL, setValidL] = useState(false);

    // A function that sends the entered data to the file upload component
    const continue_uploader_image=()=>{
        if(valid && validF && validL)
        {
            const form = [firstName, lastName, idNumber];
            navigate('/upload', { state: { data: form } })
        }
        else {
            sentNofile(true)
        }
    }

    // A function that checks the correctness of the ID number
    const is_israeli_id_number=(id)=> {
        id = String(id).trim();
        if (id.length> 9 || isNaN(id)) return false;
        id = id.length < 9 ? ("00000000" + id).slice(-9) : id;
        return Array.from(id, Number).reduce((counter, digit, i) => {
            const step = digit * ((i % 2) + 1);
            return counter + (step > 9 ? step - 9 : step);
        }) % 10 === 0;
    }

    // A function that closes the modal
    const cancelModel = () => {
       sentNofile(false)
    }

    // A function that checks the correctness of the firstName and lastName
    const hebrewLetters=(text)=>{
        const checkText = /^([\u0590-\u05FF]+)$/;
        return checkText.test(text)
    }

    return(
        <div>
            {/* Displays the personal data entry buttons */}
            <Box component="form" sx={{ '& > :not(style)': { m: 1, width: '25ch' }, }} noValidate autoComplete="off">
                <TextField required id="standard-basic" error={firstName === '' || !validF} label="FirstName" variant="standard" onChange={(event) => { setFirstName(event.target.value); setValidF(hebrewLetters(event.target.value))}} />
                <TextField required id="standard-basic" error={lastName === '' || !validL} label="LastName" variant="standard"  onChange={(event) => {setLastName(event.target.value); setValidL(hebrewLetters(event.target.value))}}/>
                <TextField required id="standard-basic" error={idNumber === '' || !valid} label="Id Number" variant="standard" onChange={(event) => { setidNumber(event.target.value); setValid(is_israeli_id_number(event.target.value)) }} />
            </Box>
            <button onClick={continue_uploader_image}  className="continue-btn" type="button">continue</button>

            {/* error modal — when not enough files were uploaded */}
            <MyModal show={noFile} title={'All fields are required, proper values must be entered'} cancelModel={cancelModel} icon={<i className="fa fa-exclamation-triangle warning-triangle col" aria-hidden="true"></i>}></MyModal>
        </div>
    )
}


