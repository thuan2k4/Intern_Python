// Like a div
import { useState } from "react";
import Message from "./Message";
import Alert from "./components/Alert";
import Button from "./components/Button";
import ListGroup from "./components/ListGroup";
function App() {
  const [alertVisible, setAlertVisibility] = useState(false)
  // let items = [
  //   'New York',
  //   'San Fracico',
  //   'Tokyo',
  //   'London',
  //   'Paris'
  // ]
  // let heading = "Cities"

  // const handleSelectItem = (item: string) => {
  //   console.log(item)
  // }

  return (
    <div>
      {/* <ListGroup heading={heading} items={items} onSelecteItem={handleSelectItem} /> */}
      {alertVisible &&
        <Alert onClose={() => { setAlertVisibility(false) }}>
          Hello World!
        </Alert>}
      <Button
        onClick={() => { setAlertVisibility(true) }}
      >
        My Button
      </Button>
    </div>
  )
}

export default App;