import './ImageDropZone.css';
import React, { useRef } from 'react'
import { useDropzone } from 'react-dropzone'
import { useState, useCallback, useImperativeHandle, forwardRef } from 'react';
import MyModal from '../modals/MyModal';
import Webcam from "react-webcam";

// An object that contains the camera settings
const videoConstraints = {
    height: 200,
    facingMode: "user"
};

const ImageDropZone = forwardRef((props, ref) => {
    // Variable settings
    const [imageFile, setImageFile] = useState();
    const [openCamera, setOpenCamera] = useState(false);
    const webcamRef = useRef(null);
    const [image, setImage] = useState('');

    // A function responsible for deleting a selected file
    const cancel = () => {
        setImageFile(undefined)
        setImage('')
    }

    // A function responsible for opening the camera
    const openCamera1 = () => {
        setOpenCamera(true)
    }

    // A function responsible for closing the camera
    const cancelModel = () => {
        if (openCamera) { setOpenCamera(false) }
    }

    // A function responsible for capturing the image
    const capture = useCallback(
        () => {
            const imageSrc = webcamRef.current.getScreenshot();
            setImage(imageSrc)
        },
        [webcamRef]
    );

    // A function responsible for saving the image
    const save = () => {
        const imageBlob = new File([image], 'File Camera', { type: 'image/png' })
        setImageFile(imageBlob)
        setOpenCamera(false)
    }

    // A function responsible for saving the uploaded image by dragging or dropping
    const onDrop = useCallback(
        acceptedFiles => {
            const file = acceptedFiles[0]
            if (file.type === 'application/pdf' || file.type === 'image/png' || file.type === 'image/jpeg') {
                setImageFile(file)
            }
        },
        [setImageFile],
    )

    // Sending the image object uploaded to the imageUploader component
    useImperativeHandle(ref, () => ({
        returnFile() {
            return imageFile
        }
    }));

    // Set the drag and drop variable
    const { getRootProps, getInputProps } = useDropzone({ onDrop })

    return (
        <div>
            <div className='image-upload-wrap' >
                {/* Button for uploading a file from the computer / dragging the file and dialog ... */}
                <div {...getRootProps()}>
                    <input className='file-upload-input' type='file' accept="image/*" {...getInputProps()} />
                    <div className='drag-text'>
                        <h3>{props.nameH3}</h3>
                        {imageFile ? <h6>{imageFile.name}</h6> : <h6>Click or drag here to upload</h6>}
                    </div>
                </div>
                {/* Cancel the selected file */}
                <div >
                    {imageFile ? <i onClick={cancel} className="fa fa-times cancel" aria-hidden="true" /> : <></>}
                </div>
                {/* Button to open the camera to take the file */}
                <div >
                    <i onClick={openCamera1} className="cameraO fa fa-camera" aria-hidden="true" />
                </div>
            </div>
            {/* modal for opening the camera */}
            <MyModal
                show={openCamera}
                title={props.nameH3}
                cancelModel={cancelModel}
                icon={<i className="fa fa-camera camera col" aria-hidden="true" />}>
                <div className="webcam-container">
                    {/* Displays the camera screen / View the captured image */}
                    <div className="webcam-img">
                        {image === '' ? <Webcam
                            audio={false}
                            ref={webcamRef}
                            screenshotFormat="image/png"
                            videoConstraints={videoConstraints}
                        /> : <img src={image} alt=''/>}
                    </div>
                    {/* Displays the save button / save and replay buttons */}
                    {image === '' ?
                        <button className='btn-camera' onClick={(e) => { e.preventDefault(); capture(); }}>Capture</button> :
                        <><button className='btn-camera' onClick={(e) => { e.preventDefault(); save(); }}>Save</button>
                            <button className='btn-camera repeat' onClick={(e) => { e.preventDefault(); setImage('') }}>Repeat</button></>}
                </div>
            </MyModal>
        </div>
    )
})
ImageDropZone.displayName = "ImageDropZone";
export default ImageDropZone;