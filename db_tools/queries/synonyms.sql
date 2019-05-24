WITH words as (
  SELECT synset_id
  FROM term
  WHERE word = {}
)
SELECT *
FROM term
       RIGHT JOIN words ON words.synset_id = term.synset_id
;
