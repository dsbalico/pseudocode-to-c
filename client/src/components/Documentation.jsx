import React from 'react'

function Documentation() {
    return (
        <div className="px-5 md:px-12 pb-8" id="documentation">
            <h2 className="text-2xl font-bold">Documentation</h2>
            
            <div className="mt-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Initializing variables</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">initialize</span> and <span className="text-blue-500">declare</span>
                
                <br/><br/>

                <span className="text-gray-400"># with value (autodetect datatype)</span>
                <br/>
                <span className="text-blue-500">initialize</span> x to <span className="text-red-500">100</span>
                
                <br/><br/>

                <span className="text-gray-400"># no value</span><br/>
                <span className="text-blue-500">initialize</span> x as (<span className="text-green-500">int</span>/<span className="text-green-500">float</span>/<span className="text-green-500">char</span>) <br />
                <span className="text-blue-500">initialize</span> <span className="text-green-500">float</span> x
                </p>
            </div>

            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Assigning variables</h4>
                <p className="bg-gray-100 dark:bg-gray-800 h-full p-5 rounded-sm font-mono text-sm">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">set</span>
                
                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">set</span> x to <span className="text-red-500">10</span> <br />
                <span className="text-blue-500">set</span> x to <span className="text-red-500">10</span> plus <span className="text-red-500">1</span> <br />
                <span className="text-blue-500">set</span> x to y (<span className="text-green-500">plus</span>/<span className="text-green-500">minus</span>/<span className="text-green-500">multiply</span>/<span className="text-green-500">divide</span>) <span className="text-red-500">10</span> <br />
                
                </p>
            </div>

            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Arithmetic Operations</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">add</span>, <span className="text-blue-500">subtract</span>, <span className="text-blue-500">multiply</span>, <span className="text-blue-500">divide</span>
                
                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">add</span> <span className="text-red-500">10</span> to x <br/>
                <span className="text-blue-500">subtract</span> <span className="text-red-500">10</span> to x <br/>
                <span className="text-blue-500">multiply</span> x by <span className="text-red-500">10</span> <br/>
                <span className="text-blue-500">divide</span> x by <span className="text-red-500">2</span>
                </p>
            </div>

            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">If-else Statements</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">if</span>, <span className="text-blue-500">elif</span>, and <span className="text-blue-500">else</span>

                <br/><br/>
                
                <span className="text-gray-400"># conditional statemetns</span>
                <br/>
                greater than, less than, equal, not equal, or, and, greater than or equal, less than or equal

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">if</span> x is greater than y <br />
                <span className="text-gray-400"># code here</span> <br />
                <span className="text-blue-500">elif</span> x is less than y <br />
                <span className="text-gray-400"># code here</span> <br />
                <span className="text-blue-500">else</span> <br />
                <span className="text-gray-400"># code here</span> <br />
                <span className="text-blue-500">endif</span>
                </p>
            </div>

            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">For loop</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">for</span> and <span className="text-blue-500">loop</span>

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">for</span> i equals <span className="text-red-500">1</span> to <span className="text-red-500">100</span> <br />
                <span className="text-gray-400"># code here</span> <br />
                <span className="text-blue-500">enfor</span> <br /><br />
                <span className="text-blue-500">loop</span> x from <span className="text-red-500">1</span> to <span className="text-red-500">100</span> <br />
                <span className="text-gray-400"># code here</span> <br />
                <span className="text-blue-500">endloop</span>
                </p>
            </div>
            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Increment & Decrement</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">increment</span> and <span className="text-blue-500">decrement</span>

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">increment</span> x <br />
                <span className="text-blue-500">decrement</span> x<br />
                </p>
            </div>
            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Print Statement</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">print</span>, <span className="text-blue-500">display</span>, <span className="text-blue-500">show</span>, <span className="text-blue-500">log</span>

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">print</span> x <span className="text-gray-400">(if x is not initialized, it will automatically print as text)</span> <br />
                <span className="text-blue-500">print</span> <span className="text-green-500">'hello world!'</span><br />
                <span className="text-blue-500">print</span> <span className="text-green-500">'x: '</span> x
                </p>
            </div>
            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">While loop</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-blue-500">while</span>

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-blue-500">while</span> x is less than <span className="text-red-500">10</span><br/>
                <span className="text-gray-400"># code here</span><br/>
                <span className="text-blue-500">endwhile</span>
                </p>
            </div>

            <div className="flex flex-col">
                <h4 className="text-xl font-medium my-2">Comments</h4>
                <p className="h-full bg-gray-100 p-5 rounded-sm font-mono text-sm dark:bg-gray-800">
                <span className="text-gray-400"># keywords</span>
                <br/>
                <span className="text-gray-400">comment</span>, <span className="text-gray-400">//</span>, <span className="text-gray-400">#</span> 

                <br/><br/>

                <span className="text-gray-400"># Examples</span>
                <br/>
                <span className="text-gray-400">comment this is a comment</span><br/>
                <span className="text-gray-400"># this is a comment</span><br/>
                <span className="text-gray-400">// this is a comment</span><br/>
                </p>
            </div>
            </div>
        </div>
    )
}

export default Documentation