import { useMemo, useState } from 'react'
import { Search, ChevronRight, ChevronDown } from 'lucide-react';
import { notes } from './notes';
import { filler_phrases } from './notes';

// const allCategories = {
//     "personal": ["introduction"],
//     "principles": [
//         "customer obsession",
//         "deliver results",
//         "dive deep",
//         "earn trust",
//         "are right, a lot",
//         "bias for action",
//         "have backbone disagree and commit",
//         "insist on the highest standards",
//         "invent and simplify",
//         "learn and be curious",
//         "think big",
//         "ownership",
//         "leadership"
//     ],
//     "situation": [
//         "conflicts resolution",
//         "teamwork collaboration",
//         "problem solving",
//         "decision making",
//         "performance and recognition",
//         "learning and development",
//         "adapatability",
//         "handling work pressure",
//         "innovative",
//         "client and stakeholder",
//         "ethical challenges",
//         "technical challenges",
//         "feedback and growth",
//         "communication",
//         "mistakes",
//         "failure",
//         "proud moments"
//       ],
//     "miscelleneous": [
        
//     ]
//   }

const InterviewNotes = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [expandedCategories, setExpandedCategories] = useState([]);

  const filterNotes = () => {
    if (!searchTerm) return notes;
  
    const filtered = {};
    const categoriesToExpand = [];
  
    Object.entries(notes).forEach(([category, items]) => {
      const filteredItems = items.filter(item => 
        Object.values(item).some(value => 
          typeof value === 'string' && 
          value.toLowerCase().includes(searchTerm.toLowerCase())
        )
      );
      
      if (filteredItems.length > 0) {
        filtered[category] = filteredItems;
        categoriesToExpand.push(category);
      }
    });
  
    setExpandedCategories(categoriesToExpand);
  
    return filtered;
  };
  
  const filteredNotes = useMemo(() => {
    return searchTerm ? filterNotes() : notes;
  }, [searchTerm, notes]);

  const categoryProps = {
    expandedCategories:expandedCategories,
    setExpandedCategories: setExpandedCategories
  }

  return (
    <div className='flex flex-row items-start justify-center w-full h-full p-10'>
        <div className='w-[75%] h-full'>
            <div className="relative w-full max-w-4xl p-4 mx-auto bg-white border border-green-300 rounded-lg shadow-lg">
                {/* Introduction button */}
                <Title title="self introduction" />
                <div className="mb-4 border rounded-lg">
                    <CategoryButton category="introduction" {...categoryProps} />
                    {expandedCategories.includes("introduction") && <IntroductionBlock />}
                </div>

                {/* Filler phrases button */}
                <Title title="Important filler phrases" />
                <div className="mb-4 border rounded-lg">
                    <CategoryButton category="fillers" {...categoryProps} />
                    {expandedCategories.includes("fillers") && <ImportantFillerPhrases />}
                </div>
                
                {/* Search Bar */}
                <div className="sticky top-0 mb-4">
                    <Search className="absolute left-3 top-2.5 text-gray-400 h-5 w-5" />
                    <input
                    type="text"
                    placeholder="Search LPs..."
                    className="w-full py-2 pl-10 pr-4 border rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-200"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>
                
                {/* Total question count */}
                <Title title="leadership principles" />
                <span className='py-2'>Total Questions: {Object.values(filteredNotes).reduce((count, questions) => count + questions.length, 0)}</span>

                {/* Leadership principle questions */}
                <div className="space-y-4">
                    {
                    Object.entries(filteredNotes).map(([category, items]) => (
                        <div key={category} className="border rounded-lg">
                            <CategoryButton category={category} items={items} {...categoryProps} />
                            {expandedCategories.includes(category) && <DisplayItems items={items} />}
                        </div>
                    ))
                    }
                </div>
            </div>
        </div>
    </div>
  );
};


const IntroductionBlock = () => {
  return (
    <div>
      p
    </div>
  )
}

const ImportantFillerPhrases = () => {
  const Separator = () => <p className='text-gray-900'><hr></hr></p>
  return (
    <ul className='w-full p-4 space-y-3'>
      {filler_phrases.map((phrase, idx) => (
        phrase.includes("#break") ? <Separator /> : <li className='ml-4 list-disc' key={idx}><span>{phrase}</span></li>
      ))}
    </ul>
    // Object.keys(filler_phrases).map((category) => (
    //   <div key={category}>
    //     <h2>{category.replace(/_/g, " ")}</h2>
    //     <ul>
    //       {Array.isArray(filler_phrases[category])
    //         ? filler_phrases[category].map((phrase, index) => (
    //             <li key={index}>{phrase}</li>
    //           ))
    //         : Object.keys(filler_phrases[category]).map((subCategory) => (
    //             <div key={subCategory}>
    //               <h3>{subCategory.replace(/_/g, " ")}</h3>
    //               <ul>
    //                 {filler_phrases[category][subCategory].map((phrase, index) => (
    //                   <li key={index}>{phrase}</li>
    //                 ))}
    //               </ul>
    //             </div>
    //           ))}
    //     </ul>
    //   </div>
    // ))
  )
}

const Title = ({title}) => <p className='text-lg font-light text-gray-400 capitalize'>{title}</p>

const DisplayItems = ({items}) => {
    return (
        <div className="p-4 space-y-4">
            {items.map((item, idx) => (
                item.question && <SingleItem key={idx} item={item} />
            ))}
            {items.length === 0 && "No items yet"}
        </div>
    )
}

const CategoryButton = ({category, items=[], expandedCategories, setExpandedCategories}) => {
    const toggleCategory = (category) => {
        setExpandedCategories(prev => 
          prev.includes(category) 
            ? prev.filter(c => c !== category)
            : [...prev, category]
        );
      };
    return (
        <button
        className="flex items-center justify-between w-full px-4 py-2 rounded-t-lg bg-gray-50 hover:bg-gray-100"
        onClick={() => toggleCategory(category)}
        >
            <span className="font-medium capitalize">{category} {items.length !== 0 && (<>({items.length})</>)}</span>
            {expandedCategories.includes(category) ? 
                <ChevronDown className="w-5 h-5" /> : 
                <ChevronRight className="w-5 h-5" />
            }
        </button>
    )
}

const SingleItem = ({item}) => {
    return (
        <div className="p-4 rounded-lg bg-gray-50">
        <div className="grid grid-cols-1 gap-2">
        <div>
            {/* <span className="font-medium text-blue-800">Question: </span> */}
            <b>{item.question}</b>
        </div>
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
            {/* <pre className="font-sans whitespace-pre-wrap">{item.action}</pre> */}
            {item.action}
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
    )
}
export default InterviewNotes;