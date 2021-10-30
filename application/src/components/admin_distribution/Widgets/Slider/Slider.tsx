import "./Slider.css"
import {useState} from "react";
import {displayOptions} from "../../../../share";

export function Slider(props: {
    question: QuestionType,
}) {
    return (
        <div className="d-flex flex-column mb-2">
            <div className="font-middle text-truncate font-weight-bold">{props.question.value}</div>
            <input style={{'filter': displayOptions[props.question.display_option].color_shifter(props.question.rate)}}
                   type="range" className="admin-slider" min={0} max={100}
                   value={props.question.rate} readOnly={true}/>
            <div className="d-flex justify-content-between font-tiny text-secondary">
                {displayOptions[props.question.display_option].text_equivalents
                    .map((value: string) => <span key={value}>{value}</span>)}
            </div>
        </div>
    )
}

export default Slider