**Text Detection/Detection/Spotting**

```json
{
"annotations": [  // List of dictionaries, one for each image.
  {
    "image_id": "the filename of corresponding image.",
    "paragraphs": [  // List of paragraphs.
      {
        "lines": [  // List of lines.
          {
            "text": "the text content of the entire line",  // Set to empty string for detection-only evaluation.
            "words": [  // List of words.
              {
                "vertices": [[x1, y1], [x2, y2],...,[xm, ym]],
                "text": "the text content of this word",  // Set to empty string for detection-only evaluation.
              }, ...
            ]
          }, ...
        ]
      }, ...
    ]
  }, ...
]
}
```
