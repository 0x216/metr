export const QUESTION_LIMIT = 5

export const displayOptions: IDisplayOptions = {
    numeric_range_optimum: {
        title: 'Optimum',
        text_equivalents: ['Nizké', 'Optimální', 'Vysoké'],
        color_shifter: (value: number) => 'hue-rotate(-' + 2 * value + 'deg)'
    },
    numeric_range_maximum: {
        title: 'Maximum',
        text_equivalents: ['Nizké', 'Střední', 'Maximální'],
        color_shifter: (value: number) => 'hue-rotate(-' + value + 'deg)'
    }
}

export default {
    displayOptions,
    QUESTION_LIMIT
}