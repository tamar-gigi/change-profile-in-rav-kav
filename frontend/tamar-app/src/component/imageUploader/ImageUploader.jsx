import './ImageUploader.css';
import React from 'react'
import ImageDropZone from '../imageDropZone/ImageDropZone';
import { useLocation, useNavigate } from 'react-router-dom';
import { useState, useRef } from 'react';
import MyModal from '../modals/MyModal';
import axios from 'axios';
import Wait from '../wait/wait'


export default function ImageUploader() {
   // Variable settings
   const [noFile, sentNofile] = useState(false)
   const idCardRef = useRef();
   const studantPermitRef = useRef();
   const studentCardRef = useRef();
   const ravKavRef = useRef();
   const navigate = useNavigate();
   const [invalideFiles, setInvalideFile] = useState(false);
   const [res, setRes] = useState([]);
   const location = useLocation();
   const [showWait, setShowWait]=useState(false);

   // A function that sends the server to the files
   const send = () => {
      // When all files are present
      if (idCardRef.current.returnFile() && studantPermitRef.current.returnFile() && studentCardRef.current.returnFile() && ravKavRef.current.returnFile()) {
         const idCard = idCardRef.current.returnFile()
         const studantPermit = studantPermitRef.current.returnFile()
         const studentCard = studentCardRef.current.returnFile()
         const ravKav = ravKavRef.current.returnFile()
         const firstName = location.state.data[0]
         const lastName = location.state.data[1]
         const idNumber = location.state.data[2]
         console.log(ravKavRef.current.returnFile())
         // Create from all files one FormData object that is sent to the server
         const formData = new FormData();
         formData.append('firstName',firstName);
         formData.append('lastName', lastName);
         formData.append('idNumber', idNumber);
         formData.append('idCard', idCard);
         formData.append('studentPermit', studantPermit);
         formData.append('studentCard', studentCard);
         formData.append('ravKav', ravKav);

         // Send to server
         axios.post('http://127.0.0.1:5000/upload-images', formData, { 
            onUploadProgress:()=>setShowWait(true)
         })
            // Getting the answer from the server
            .then(response => {
               setShowWait(false)
               if (response.data[0] === '1') { rout() }
               if (response.data[0] === '0') { responseFalse(response.data[1]) }
            })
            .catch((error) => {
               if (error.response) {
                  console.log(error.response)
                  console.log(error.response.status)
                  console.log(error.response.headers)
               }
            })
      }
      // In case all files are not uploaded, an appropriate message is displayed
      else {
         sentNofile(true)
      }
   }

   // When a negative response is returned from the server, show the modal of the invalid files
   const responseFalse = (re) => {
      setRes(re)
      setInvalideFile(true)
   }
   // When a positive response is returned from the server, send for further operation
   const rout = () => {
      navigate('/continue')
   }

   // A function that closes the modal
   const cancelModel = () => {
      if (noFile) { sentNofile(false) }
      if (invalideFiles) { setInvalideFile(false); navigate('/') }
   }

   return (
      <div className='all'>
         <Wait show={showWait}/>

         <h3>Please upload the appropriate photos</h3>
         {/* The component of uploading files */}
         <div className='imageDropzone'>
            <ImageDropZone ref={idCardRef} nameH3={"Id card"} />
            <ImageDropZone ref={studantPermitRef} nameH3={"Student Permit"} />
         </div>
         <div className='imageDropzone'>
            <ImageDropZone ref={studentCardRef} nameH3={"Student card"} />
            <ImageDropZone ref={ravKavRef} nameH3={"Rav kav Card"} />
         </div>


         {/* Button of sending the files */}
         <button onClick={send} className="file-upload-btn" type="button" onKeyPress={(e) => {
            if (e.key === "Enter") {
               send()
            }
         }} >I finished<i className="fa fa-paper-plane send" aria-hidden="true"></i></button>

         {/* error modal — when not enough files were uploaded */}
         <MyModal show={noFile} title={'All appropriate forms must be uploaded'} cancelModel={cancelModel} icon={<i className="fa fa-exclamation-triangle warning-triangle col" aria-hidden="true"></i>}></MyModal>
       
         {/* error modal — when a negative response is returned from the server */}
         <MyModal show={invalideFiles} title={'Invalide files'} cancelModel={cancelModel} icon={<i className="fa fa-exclamation-triangle warning-triangle col" aria-hidden="true"></i>}>
            {res ? res.map((re, index) => {
               return (<div key={index}>{re}</div>)
            }) : ''}
         </MyModal>

   
      </div>
   )
}

