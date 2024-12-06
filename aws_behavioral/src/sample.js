import { useEffect, useState } from 'react'
import { Search, ChevronRight, ChevronDown } from 'lucide-react';
import { notes } from './notes';


const InterviewNotes = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTags, setSelectedTags] = useState([]);
  const [expandedCategories, setExpandedCategories] = useState(['customer obsession']);
  const [allTags, setAllTags] = useState([
    'led', 'leadership', 'teamwork', 'conflict', 'migration', 'performance', 
    'failure', 'success', 'technical', 'communication', 'project'
  ]);

//   const [filteredNotes, setFilteredNotes] = useState(notes);

//   useEffect(() => {
//     setFilteredNotes(() => {
//         var all_notes = notes;
//         if (searchTerm) {
//             all_notes = filterNotes(searchTerm);
//         }
//         if (selectedTags) {
//             var current_notes = [];
//             for (let i = 0; i < selectedTags.length; i++) {
//                 current_notes =
//               }
//         }
//         return all_notes;
//     }
//     );
//   }, [searchTerm, selectedTags])

  const toggleCategory = (category) => {
    setExpandedCategories(prev => 
      prev.includes(category) 
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  const toggleTag = (tag) => {
    setSelectedTags(prev => 
      prev.includes(tag) 
        ? prev.filter(t => t !== tag)
        : [...prev, tag]
    );
  };

  const filterNotes = (search_item) => {
    const filtered = {};
    Object.entries(notes).forEach(([category, items]) => {
        const searchTags = selectedTags;
        searchTags.every(
            tag => {
                const filteredItems = items.filter(item => 
                  Object.values(item).some(value => 
                    value.toLowerCase().includes(tag.toLowerCase())
                  )
                );
                if (filteredItems.length > 0) {
                  filtered[category] = filteredItems;
                }
            }
        )
    });
    return filtered;
  };


  const filteredNotes = (searchTerm || selectedTags.length) ? filterNotes(searchTerm) : notes;

  return (
    <div className='w-full h-full flex flex-row justify-center items-start p-10'>
        <div className='w-[75%] h-full'>
            <div className="w-full max-w-4xl mx-auto p-4 bg-white rounded-lg border border-green-300 shadow-lg">
                <div className="mb-4 relative">
                    <Search className="absolute left-3 top-2.5 text-gray-400 h-5 w-5" />
                    <input
                    type="text"
                    placeholder="Search your notes..."
                    className="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>

                <div className="space-y-4">
                    {Object.entries(filteredNotes).map(([category, items]) => (
                    <div key={category} className="border rounded-lg">
                        <button
                        className="w-full px-4 py-2 flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-t-lg"
                        onClick={() => toggleCategory(category)}
                        >
                        <span className="font-medium capitalize">{category}</span>
                        {expandedCategories.includes(category) ? 
                            <ChevronDown className="h-5 w-5" /> : 
                            <ChevronRight className="h-5 w-5" />
                        }
                        </button>
                        
                        {expandedCategories.includes(category) && (
                        <div className="p-4 space-y-4">
                            {items.map((item, idx) => (
                            <div key={idx} className="bg-gray-50 p-4 rounded-lg">
                                <div className="grid grid-cols-1 gap-2">
                                <div>
                                    <span className="font-medium text-blue-600">Situation: </span>
                                    {item.situation}
                                </div>
                                <div>
                                    <span className="font-medium text-blue-600">Task: </span>
                                    {item.task}
                                </div>
                                <div>
                                    <span className="font-medium text-blue-600">Action: </span>
                                    <pre className="whitespace-pre-wrap font-sans">{item.action}</pre>
                                </div>
                                <div>
                                    <span className="font-medium text-blue-600">Result: </span>
                                    {item.result}
                                </div>
                                {item.edge_case && <div>
                                    <span className="font-medium text-blue-600">Edge Case: </span>
                                    {item.edge_case}
                                </div>}
                                </div>
                            </div>
                            ))}
                        </div>
                        )}
                    </div>
                    ))}
                </div>
                {filteredNotes.length === 0 && (
                    <div className="text-center py-8 text-gray-500">
                    No notes match your search criteria
                    </div>
                )}
            </div>
        </div>
        <div className="w-64">
        <div className="bg-white rounded-lg shadow p-4 sticky top-4">
          <h3 className="font-medium mb-4">Filter by Tags</h3>
          <div className="space-y-2">
            {allTags.map(tag => (
              <button
                key={tag}
                onClick={() => toggleTag(tag)}
                className={`w-full px-3 py-2 rounded-lg text-left text-sm ${
                  selectedTags.includes(tag)
                    ? 'bg-blue-500 text-white'
                    : 'bg-gray-50 text-gray-700 hover:bg-gray-100'
                }`}
              >
                #{tag}
                <span className="float-right">
                    {Object.entries(notes).map(([category, items]) => (
                        items.filter(item => item.tags.includes(tag)).length
                    ))}
                </span>
              </button>
            ))}
          </div>
        </div>
      </div>
        {/* <div className="w-64 bg-white rounded-lg shadow-lg p-4">
            <h3 className="font-medium mb-4">Tags</h3>
            {selectedTags.map(tag => <p>{tag}</p>)}

                <div className="flex flex-wrap gap-2">
                {allTags.map(tag => (
                    <button
                    key={tag}
                    onClick={() => toggleTag(tag)}
                    className={`px-3 py-1 rounded-full text-sm ${
                        selectedTags.includes(tag)
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                    >
                    {tag}
                    </button>
                ))}
            </div>
        </div> */}
    </div>
  );
};

export default InterviewNotes;




// import { useMemo, useState } from 'react'
// import { Search, ChevronRight, ChevronDown } from 'lucide-react';
// import { sample_notes as notes } from './notes';


// const InterviewNotes = () => {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [expandedCategories, setExpandedCategories] = useState([]);
//   const [expandedSubCategories, setExpandedSubCategories] = useState([]);

//   const toggleCategory = (category) => {
//     setExpandedCategories(prev => 
//       prev.includes(category) 
//         ? prev.filter(c => c !== category)
//         : [...prev, category]
//     );
//   };

//   const filterNotes = () => {
//     if (!searchTerm) return notes;
  
//     const filtered = {};
//     const categoriesToExpand = [];
  
//     Object.entries(notes).forEach(([category, items]) => {
//       const filteredItems = items.filter(item => 
//         Object.values(item).some(value => 
//           typeof value === 'string' && 
//           value.toLowerCase().includes(searchTerm.toLowerCase())
//         )
//       );
      
//       if (filteredItems.length > 0) {
//         filtered[category] = filteredItems;
//         categoriesToExpand.push(category);
//       }
//     });
  
//     setExpandedCategories(categoriesToExpand);
  
//     return filtered;
//   };
  
//   const filteredNotes = useMemo(() => {
//     return searchTerm ? filterNotes() : notes;
//   }, [searchTerm, notes]);

//   return (
//     <div className='w-full h-full flex flex-row justify-center items-start p-10'>
//         <div className='w-[75%] h-full'>
//             <div className="w-full max-w-4xl mx-auto p-4 bg-white rounded-lg border border-green-300 shadow-lg">
//                 <div className="mb-4 relative">
//                     <Search className="absolute left-3 top-2.5 text-gray-400 h-5 w-5" />
//                     <input
//                     type="text"
//                     placeholder="Search your notes..."
//                     className="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-200"
//                     value={searchTerm}
//                     onChange={(e) => setSearchTerm(e.target.value)}
//                     />
//                 </div>
//                 <span className='py-2'>Total Question: {Object.values(filteredNotes).reduce((count, questions) => count + questions.length, 0)}</span>
//                 <div className="space-y-4">
//                     {Object.entries(filteredNotes).map(([category, items]) => (
//                     <div key={category} className="border rounded-lg">
//                         <button
//                         className="w-full px-4 py-2 flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-t-lg"
//                         onClick={() => toggleCategory(category)}
//                         >
//                             <span className="font-medium capitalize">{category} ({items.length})</span>
//                             {expandedCategories.includes(category) ? 
//                                 <ChevronDown className="h-5 w-5" /> : 
//                                 <ChevronRight className="h-5 w-5" />
//                             }
//                         </button>
                        
//                         {expandedCategories.includes(category) && (
//                         <div className="p-4 space-y-4">
//                             {items.map((item, idx) => (
//                                 item.question && <SingleItem key={idx} item={item} />
//                             ))}
//                             {items.length === 0 && "No items yet"}
//                         </div>
//                         )}
//                     </div>
//                     ))}
//                 </div>
//             </div>
//         </div>
//     </div>
//   );
// };

// const SingleItem = ({item}) => {
//     return (
//         <div className="bg-gray-50 p-4 rounded-lg">
//         <div className="grid grid-cols-1 gap-2">
//         <div>
//             {/* <span className="font-medium text-blue-800">Question: </span> */}
//             <b>{item.question}</b>
//         </div>
//         <div>
//             <span className="font-medium text-blue-600">Situation: </span>
//             {item.situation}
//         </div>
//         <div>
//             <span className="font-medium text-blue-600">Task: </span>
//             {item.task}
//         </div>
//         <div>
//             <span className="font-medium text-blue-600">Action: </span>
//             {/* <pre className="whitespace-pre-wrap font-sans">{item.action}</pre> */}
//             {item.action}
//         </div>
//         <div>
//             <span className="font-medium text-blue-600">Result: </span>
//             {item.result}
//         </div>
//         {item.edge_case && <div>
//             <span className="font-medium text-blue-600">Edge Case: </span>
//             {item.edge_case}
//         </div>}
//         </div>
//     </div>
//     )
// }
// export default InterviewNotes;