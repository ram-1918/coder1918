import { useMemo, useState } from 'react'
import { Search, ChevronRight, ChevronDown } from 'lucide-react';
import { notes, filler_phrases, introduction } from './notes';
import parse from 'html-react-parser';

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

  // Parsing function with custom components

const ulStyle = 'w-full p-4 space-y-3';
const liStyle = 'ml-4 list-disc';

  const renderFormattedText = (text) => {
  // Define tag mappings
  const tagStyles = {
    red: 'text-red-500',
    blue: 'font-semibold text-blue-600',
    green: 'font-semibold text-green-700',
    highlight: 'bg-yellow-200',
    bold: 'font-bold',
    italic: 'italic',
    imp: 'font-bold text-green-500',
    impnote: 'bg-gray-200 p-1 rounded-lg before:content-["Note"] before:text-red-500 before:font-bold'
  };

  // Replace custom tags with styled spans
  let processedText = text;
  
  Object.entries(tagStyles).forEach(([tag, className]) => {
    const regex = new RegExp(`<${tag}>(.*?)<\\/${tag}>`, 'g');
    processedText = processedText.replace(
      regex, 
      `<span class="${className}">$1</span>`
    );
  });

  return parse(processedText);
};

  
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
  }, [searchTerm]);

  const categoryProps = {
    expandedCategories:expandedCategories,
    setExpandedCategories: setExpandedCategories
  }

  return (
    <div className='flex flex-row items-start justify-center w-full h-full p-10 mobile:p-0 mobile:text-sm tablet:text-xl laptop:text-2xl tablet:bg-red-400'>
        <div className='w-full h-full'>
            <header className='fixed top-0 left-0 right-0 z-10 h-10 bg-gray-100'>
              <div className='flex items-center justify-start w-full h-full px-4 space-x-4 mobile:px-2'>
                <a href="#introduction">Introduction</a>
                <a href="#phrases">Phrases</a>
                <a href="#lps">Leaderships</a>
              </div>
            </header>
            <div className="relative w-full max-w-4xl p-4 mx-auto mt-10 bg-white border border-green-300 rounded-lg shadow-lg mobile:p-2 mobile:w-full">
                {/* Introduction button */}
                <Title id="introduction" title="self introduction" />
                <div className="mb-4 border rounded-lg">
                    <CategoryButton category="introduction" {...categoryProps} />
                    {expandedCategories.includes("introduction") && <IntroductionBlock />}
                </div>

                {/* Filler phrases button */}
                <Title id="phrases" title="Important filler phrases" />
                <div className="mb-4 border rounded-lg">
                    <CategoryButton category="fillers" {...categoryProps} />
                    {expandedCategories.includes("fillers") && <ImportantFillerPhrases />}
                </div>
                
                {/* Search Bar */}
                <div className="sticky mt-1 mb-4 top-10">
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
                <Title id="lps" title="leadership principles" />
                <span className='py-2 text-gray-300 tablet:text-md laptop:text-lg'>Total Questions: {Object.values(filteredNotes).reduce((count, questions) => count + questions.length, 0)}</span>

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
    <ul className={ulStyle}>
      {introduction.introduction.map((point,idx) => (
        <li key={idx} className={liStyle}>{renderFormattedText(point)}</li>
      ))}
    </ul>
  )
}

const ImportantFillerPhrases = () => {
  const Separator = () => <p className='w-full border border-gray-200'></p>
  return (
    <ul className={ulStyle}>
      {filler_phrases.map((phrase, idx) => (
        phrase.includes("#break") ? <Separator key={idx} /> : <li className={liStyle} key={idx}><span>{phrase}</span></li>
      ))}
    </ul>
  )
}

const Title = ({id,title}) => <p id={id} className='text-lg font-light text-gray-400 capitalize tablet:text-lg laptop:text-2xl'>{title}</p>

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