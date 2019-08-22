## Task №3
### Test cases for API tests

<table>
  <tr>
    <th>Title</th>
    <th>Test data</th>
    <th>Test steps</th>
    <th>Expected result</th>
  </tr>
  <tr>
    <td>Verify that required fields are needed when validating</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories</code> 
            </li>
            <li>
                <b>required fields:</b> <code>/helper/required_params_categories.json</code>
            </li>
        </ul>
    </td>
    <td>
        <ol>
            <li>Send post request with parameters</li>
            <li>Compare id in param and id in response body</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 400</li>
            <li>The amounts should be the same</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify category creation when valid category data is passed</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories</code> 
            </li>
            <li>
            <b>param:</b> <code>{"name": "Test Category", "id": random}</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send post request with parameters</li>
            <li>Compare id in param and id in response body</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 201</li>
            <li>The ids should be the same</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify get category by id </td>
    <td>
    <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories/</code>
            </li>
            <li>                
                <b>category id:</b> <code>/helper/required_params_categories.json</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request with id</li>
            <li>Compare category body in json and response body</li>
            <li>Compare name in json and name in response body</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 200</li>
            <li>The bodies should be the same</li>
            <li>The names should be the same</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify get category by id with select name</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories/</code> 
            </li>
            <li>
                <b>category id:</b> <code>/helper/required_params_categories.json</code> 
            </li>
            <li>
                <b>endpoint:</b> <code>?$select[]=name</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request with id + endpoint</li>
            <li>Compare id in json and id in response body</li>
            <li>Compare name in json and name in response body</li>
            <li>Check that only two fields in response</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 200</li>
            <li>The ids should be the same</li>
            <li>The names should be the same</li>
            <li>The response has two fields</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify get category by wrong id</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories/</code> 
            </li>
            <li>
                <b>category id:</b> 123
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request with id </li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 404</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify get default list</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request</li>
            <li>Check that response has a field "total"</li>
            <li>Check that field "data" has ten fields</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 200</li>
            <li>The response has a field "total"</li>
            <li>The field "data" has ten fields</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify allows pagination</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories</code> 
            </li>
            <li>
                <b>endpoint:</b><code>?$limit=15&$skip=15</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request with endpoin</li>
            <li>Check that field "skip" equal 15</li>
            <li>Check that field "data" has 15 fields</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 200</li>
            <li>The field "skip" equal 15"</li>
            <li>The field "data" has 15 fields</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td>Verify search on partial category name</td>
    <td>
        <ul>
            <li>
                <b>url</b> = <code>http://localhost:3030/categories</code> 
            </li>
            <li>
                <b>endpoint:</b> <code>?name[$like]=*TV*</code>
            </li>
    </td>
     <td>
        <ol>
            <li>Send get request with endpoin</li>
            <li>Check that field "data" has fields more than 0</li>
        </ol>
    </td>
    <td>
        <ol>
            <li>Get response with status code = 200</li>
            <li>The field "data" has more than 0 fields</li>
        </ol>
    </td>
  </tr>  
</table>