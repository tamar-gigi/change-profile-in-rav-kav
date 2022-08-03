import React from 'react'
import logo from '../../one-logo.svg'
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Toolbar from '@mui/material/Toolbar';

export default function Header() {
    return (     
        <AppBar style={{ background: '#342d6e'}}>
            {/* Logo - routing to the main screen */}
            <Container>
                <Toolbar disableGutters>
                    <Typography  component="a" href="/">
                         <img src={logo} style={{ maxHeight: '50px',left: '5%', top: '10%', position: 'absolute' }} alt='' />
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    )
};
