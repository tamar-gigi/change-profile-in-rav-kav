import './App.css';
import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import ImageUploader from './component/imageUploader/ImageUploader';
import { Route, Routes } from 'react-router-dom';
import TrueResponse from './component/trueResponse/TrueResponse';
import Form from './component/form/Form';
import Header from './component/header/Header';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <Routes>
          <Route path='/' element={<Form />} />
          <Route path='/upload' element={<ImageUploader />} />
          <Route path='/continue' element={<TrueResponse />} />
        </Routes>
      </header>
    </div>

  );
}

export default App;



