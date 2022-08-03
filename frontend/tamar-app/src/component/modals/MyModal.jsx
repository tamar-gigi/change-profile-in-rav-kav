import { Modal, Button } from 'react-bootstrap'

export default function MyModal(props) {
    return (
        <Modal dir="rtl" show={props.show} aria-labelledby="contained-modal-title-vcenter" centered>
            {/* Displays the appropriate diameter of the modal */}
            <Modal.Header>
                <Modal.Title className='row warning'>{props.icon}<div className='warning-text col'>{props.title}</div></Modal.Title>
            </Modal.Header>
            {/* When it is necessary to also add a body to the modal (in the camera trail) */}
            {props.children?
                <Modal.Body style={{'textAlign':'center'}}>
                    {props.children}
                </Modal.Body>:<></>}
            {/* Modal close button */}
            <Modal.Footer dir="rtl">
                <Button onClick={props.cancelModel} variant="secondary" className='btm-model'>
                    Close
                </Button>
            </Modal.Footer>
        </Modal>
    )
}