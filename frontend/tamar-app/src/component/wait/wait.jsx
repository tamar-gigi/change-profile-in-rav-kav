import * as React from 'react';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box'
import { Modal} from 'react-bootstrap'

export default function Wait(props) {

    return (
        <Modal {...props} aria-labelledby="contained-modal-title-vcenter" centered>
            <Modal.Body style={{ 'textAlign': 'center', justifyContent: 'center', alignContent: 'center'}}>
                <Box sx={{ display: 'flex',paddingLeft:'46%' }}>
                    <CircularProgress style={{ 'color': '#8ce95d' }} />
                </Box>
                <div>Processing request, please wait</div>
            </Modal.Body>
        </Modal>
    );
}

