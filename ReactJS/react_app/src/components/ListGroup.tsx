import { MouseEvent, useState } from "react"

interface Props {
    items: string[];
    heading: string;
    // (item: string) => void: function return void
    onSelecteItem: (item: string) => void
}

function ListGroup(props: Props) {
    // Hook
    const [selectedIndex, setSelectedIndex] = useState(-1)
    const [name, setName] = useState('')

    // Event handler
    const handleClick = (event: MouseEvent) => console.log(event)

    const getMessage = () => {
        return props.items.length === 0 ? <p>No item found</p> : null
    }
    props.heading = ""

    return (
        <>
            <h1>{props.heading}</h1>
            {getMessage()}
            <ul className="list-group">
                {/* arrow  function*/}
                {props.items.map((item, index) => (
                    <li
                        className={selectedIndex === index ? 'list-group-item active' : 'list-group-item'}
                        key={item}
                        onClick={() => {
                            setSelectedIndex(index)
                            props.onSelecteItem(item)
                        }}
                    >
                        {item}
                    </li>
                ))}
            </ul>
        </>
    )
}

export default ListGroup