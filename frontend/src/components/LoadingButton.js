
import React, { useState, useEffect } from 'react';
import { makeStyles } from '@mui/styles';
import Button from '@mui/material/Button'
import Typography from '@mui/material/Typography';
import {CircularProgress} from "@mui/material"
import { LoadingButton } from '@mui/lab';
const useStyles = makeStyles({
    button: {
        padding: "15px !important",
        marginLeft: "auto !important",
        marginRight: "10px !important",
        marginTop:"5px"
        
    },
    wrapper: {
        display: "flex",
        justifyContent: "space-between"
    }
})
export default function CustomLoadingButton(props) {
    const classes = useStyles()
    return <>
        <div className={classes.wrapper}>
            <div></div>
            <div></div> 
           
            <Button className={classes.button}
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
                disabled
                size="medium" > Wait...</Button>
        </div>
    </>
}