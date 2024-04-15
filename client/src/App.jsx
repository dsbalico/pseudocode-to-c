import axios from "axios";
import js_beautify from "js-beautify";
import { highlight, languages } from 'prismjs';
import 'prismjs/components/prism-c';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-coy.css';
import { useEffect, useState } from 'react';
import { AiOutlineCopy } from 'react-icons/ai';
import { BiCodeAlt } from 'react-icons/bi';
import { CgEnter } from 'react-icons/cg';
import { FaCog } from 'react-icons/fa';
import Editor from 'react-simple-code-editor';
import Documentation from "./components/Documentation";

function App() {
  const [darkmode, setDarkmode] = useState(false);
  const [pseudocode, setPseudocode] = useState("")
  const [cLanguage, setCLanguage] = useState('')

  const hightlightWithLineNumbers = (input, language) =>
    highlight(input, language)
      .split("\n")
      .map((line, i) => `<span class='editorLineNumber'>${i + 1}</span>${line}`)
      .join("\n");

  function copyCode() {
    navigator.clipboard.writeText(cLanguage);

    const copyIndicator = document.getElementById('copyIndicator');

    copyIndicator.classList.remove('hidden');

    setTimeout(() => {
      copyIndicator.classList.add('hidden');
    }, 2048)
  }

  async function submit() {  
    const loading = document.getElementById('loading');
    loading.classList.remove('hidden');

    let processed_pseudocode = pseudocode.replace(/^\s+/gm, "")
    
    const data = {
      "pseudocode": processed_pseudocode
    }
    
    await axios.post(`${import.meta.env.VITE_API}/pseudocode-to-c`, data)
      .then(res => {
        let beautifiedCode = js_beautify.js_beautify(res.data, { indent_size: 2, space_in_empty_paren: true });
        setCLanguage(beautifiedCode);
        loading.classList.add('hidden');
      })
  }

  useEffect(() => {
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      setDarkmode(true);
    } else {
      
      setDarkmode(false);
    }

    if(darkmode) 
      document.body.classList.add('dark')
    else
      document.body.classList.remove('dark');
      
  }, [darkmode])

  return (
    <div className="dark:bg-gray-900 dark:text-white transition">
      <p id="copyIndicator" className="fixed bottom-4 hidden w-full text-center">
        <span className="bg-blue-600 px-8 py-1.5 text-white font-medium shadow-md rounded-lg">Copied!</span>
      </p>
      <nav className="w-full z-10 transition dark:bg-gray-900 dark:text-white shadow fixed top-0 sm:flex justify-between bg-white px-5 py-5 md:px-12">
        <h1 className="text-xl font-bold flex gap-1.5 justify-center">
          <BiCodeAlt className="text-3xl self-center text-blue-500" /> 
          <span className="self-center">Pseudocode to C</span>
        </h1>

        <div className="flex gap-6 self-center justify-center mt-2 sm:mt-0">
          <a className="hover:text-gray-200 transition" href="#documentation">Help</a>
          <a className="hover:text-gray-200 transition" href="#about">About</a>
          
          <label className="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" className="sr-only peer" checked={darkmode} onChange={() => {
              if (localStorage.theme === 'dark') {localStorage.theme = 'light'; setDarkmode(false)}
              else {localStorage.theme = 'dark'; setDarkmode(true)}
            }} />
            <div className="w-11 h-6 bg-gray-100 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-500 dark:peer-checked:bg-blue-500"></div>
            <span className="ml-2">Dark Mode</span>
          </label>
        </div>
      </nav>
      
      <h1 className="pt-36 sm:pt-28 justify-center text-center text-gray-900 tracking-tight text-3xl font-bold dark:text-white">
        Pseudocode to C
      </h1>
      <p className="text-center px-5">A tool that allows users to easily convert pseudocode to C programming language.</p>

      <div className="flex px-5 pb-28 pt-12 md:my-0 md:px-12 flex-wrap md:flex-nowrap gap-8 h-full self-center">
        {/* Pseudocode Area */}
        <div className="w-full self-center">
          <p className="text-xl font-medium mb-2">Enter Pseudocode Here:</p>
          <div className="h-96 border border-gray-300 rounded-sm dark:border-gray-700 overflow-scroll">
            <Editor
              className="editor rounded-sm dark:bg-gray-900"
              textareaId="codeArea"
              value={pseudocode}
              onValueChange={pseudocode => setPseudocode(pseudocode)}
              highlight={pseudocode => hightlightWithLineNumbers(pseudocode, languages.python)}
              padding={10}
              style={{
                fontFamily: '"Fira code", "Fira Mono", monospace',
                fontSize: 12,
                outline: 0
              }}
            />
          </div>

          <button type="button" onClick={() => submit()} className="mt-4 border w-full py-3 border-gray-900 dark:border-white rounded-sm font-medium flex justify-center gap-1 hover:bg-blue-200 dark:hover:bg-blue-900 transition-all duration-300"><CgEnter className="self-center text-xl text-blue-500" /> Convert to C Code</button>
        </div>
        
        {/* Generated C Code Area */}
        <div className="w-full self-center">
          <p className="text-xl font-medium mb-2 flex gap-2">Generated C Code: <FaCog id="loading" className="hidden self-center text-blue-800 animate-spin dark:text-blue-500" /></p>
          <div className="h-96 border border-gray-300 rounded-sm dark:border-gray-700 overflow-scroll">
            <Editor
              className="editor rounded-sm dark:bg-gray-900"
              textareaId="codeArea"
              value={cLanguage}
              onValueChange={cLanguage => setCLanguage(cLanguage)}
              highlight={cLanguage => hightlightWithLineNumbers(cLanguage, languages.c)}
              padding={10}
              style={{
                fontFamily: '"Fira code", "Fira Mono", monospace',
                fontSize: 12,
                outline: 0
              }}
            />
          </div>

          <button onClick={() => copyCode()} className="mt-4 border w-full py-3 border-gray-900 dark:border-white dark:text-white rounded-sm text-gray-900 font-medium flex justify-center gap-1 hover:bg-blue-300 dark:hover:bg-blue-900 transition-all duration-300"><AiOutlineCopy className="self-center text-blue-500 text-xl" />Copy Code</button>
        </div>
      </div>
      
      <Documentation />
      
      <footer id="about" className="flex justify-between px-5 md:px-12 py-4 text-gray-500 dark:bg-gray-800 dark:text-gray-400 text-sm bg-gray-100">
        <h1 className="text-lg self-center text-gray-900 dark:text-white font-bold justify-center flex gap-1"><BiCodeAlt className="text-3xl self-center text-blue-500 dark:text-blue-600" /> <span className="self-center">Pseudocode to C</span></h1>

        <p className="self-center">© 2022 DSBalico. All Rights Reserved.</p>
      </footer>
    </div>
  )
}

export default App
