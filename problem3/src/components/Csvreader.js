import React, { Component } from 'react';
import papa from 'papaparse';
import Dropzone from 'react-dropzone';

export default class Csvreader extends Component {
    constructor() {
        super();
        this.state = {
            headers: [],
            result : [],
            dataLoaded: false
        }
    }

    //callback function to send data back up to App.js
    sendDataToApp = () => {
        this.props.dataCallback({
            "data": this.state.result,
            "dataLoaded": this.state.dataLoaded,
            "headers": this.state.headers
        })
    }

    //formats to JSON-like format for React-Table
    completeCSV = (results) => {
        let lines=results.data;
        this.setState({
            headers: lines[0],
            dataLoaded: true
        });

        for(let i=1;i<lines.length;i++){
            let obj = {};
            let currentline=lines[i];
            obj["row"]=i;
            for(let j=0;j<this.state.headers.length;j++){
                obj[this.state.headers[j]] = currentline[j];
            }
            this.state.result.push(obj);
        }
        this.sendDataToApp();
    }

    //reads in the CSV
    onDrop = (e) => {
    const reader = new FileReader();
        reader.onload = () => {
            papa.parse(reader.result, {
                dynamicTyping: true,
                complete: this.completeCSV
            });
        };
        
        reader.readAsBinaryString(e[0]);
    }

    render() {
        return (
            <div>
                <Dropzone 
                    name={"csvdrop"} 
                    onDrop={this.onDrop} 
                    style={{
                        height: "100%",
                        width: "100vw",
                        border: "4px dashed"
                    }}>
                    <p style={{position: "relative", top: "50%", transform: "translateY(-50%)"}}>Drag and drop a CSV file here, or click to select a CSV file to upload.</p>
                </Dropzone>
            </div>
        )
    }
}